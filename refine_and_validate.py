import requests
import json
import time
import sys
from concurrent.futures import ThreadPoolExecutor

# Ensure output handles Romanian characters correctly
sys.stdout.reconfigure(encoding='utf-8')

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

CATEGORIES = [
    "Sports & Rivalry",
    "Online Forums & Social Media",
    "Politics & Public Personalities",
    "Hate Speech & Discriminatory",
    "General Aggression & Insults",
    "Misogyny & Objectification",
    "Ableism & Mental Stigma",
    "Family & Religious Invective"
]

def classify_and_validate(text):
    prompt = f"""
Ești un expert în moderarea conținutului și lingvistică română. 
Analizează următoarea frază și încadreaz-o în CEA MAI POTRIVITĂ categorie din lista de mai jos.

FRAZA: "{text}"

CATEGORII POSIBILE:
1. Sports & Rivalry (insulte legate de echipe, arbitri, meciuri)
2. Online Forums & Social Media (troli, certuri pe net, insulte despre postări)
3. Politics & Public Personalities (insulte la adresa politicienilor, guvernului, legilor)
4. Hate Speech & Discriminatory (rasism, xenofobie, homofobie, ură etnică)
5. General Aggression & Insults (înjurături generice fără context specific)
6. Misogyny & Objectification (sexism, insulte la adresa femeilor)
7. Ableism & Mental Stigma (insulte despre dizabilități, boli mintale, "retardat", "autist")
8. Family & Religious Invective (înjurături de morți, familie, religie, sfinți)

CERINȚE:
- Dacă fraza NU este toxică sau este de neînțeles, răspunde cu categoria "REMOVE".
- Răspunde strict în format JSON: {{"category": "nume_categorie", "is_toxic": true/false}}
- Nu oferi explicații.

Răspuns JSON:"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "format": "json"
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=30)
        if response.status_code == 200:
            result = response.json().get('response', '{}')
            return json.loads(result)
        return {"category": "ERROR", "is_toxic": False}
    except Exception:
        return {"category": "ERROR", "is_toxic": False}

def process_batch():
    input_file = 'dataset_v2_synthetic.json'
    output_file = 'dataset_v3_refined_test.json'
    batch_size = 500

    print(f"--- Refinement & Re-classification (Test Batch: {batch_size}) ---")
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading {input_file}: {e}")
        return

    # Specifically target the "General Aggression" pool for re-classification
    general_pool = [d for d in data if d['category'] == "General Aggression & Insults"]
    test_batch = general_pool[:batch_size]
    other_data = [d for d in data if d['category'] != "General Aggression & Insults"]

    refined_results = []
    
    print(f"Processing {batch_size} entries from 'General Aggression'...")
    
    start_time = time.time()
    for i, entry in enumerate(test_batch):
        print(f"[{i+1}/{batch_size}] Analyzing: {entry['text'][:50]}...", end="\r")
        analysis = classify_and_validate(entry['text'])
        
        category = analysis.get('category', 'General Aggression & Insults')
        is_toxic = analysis.get('is_toxic', True)

        if category != "REMOVE" and is_toxic:
            # If the LLM found a better category, use it; otherwise keep original
            final_category = category if category in CATEGORIES else "General Aggression & Insults"
            refined_results.append({"text": entry['text'], "category": final_category})
        
        # Periodic saving/logging
        if (i+1) % 50 == 0:
            elapsed = time.time() - start_time
            print(f"\n[Progress] {i+1} entries done. Time: {elapsed:.2f}s")

    # Combine refined test batch with the rest of the original data (for completeness)
    final_output = other_data + refined_results
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(final_output, f, ensure_ascii=False, indent=2)

    print(f"\n--- Refinement Finished ---")
    print(f"Results saved to {output_file}")
    
    # Calculate new stats for the 500 processed items
    new_counts = {}
    for d in refined_results:
        cat = d['category']
        new_counts[cat] = new_counts.get(cat, 0) + 1
    
    print("\nRe-classification Stats for the 500 samples:")
    for cat, count in new_counts.items():
        print(f" - {cat}: {count}")

if __name__ == "__main__":
    process_batch()
