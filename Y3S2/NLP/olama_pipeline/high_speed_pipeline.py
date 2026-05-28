import requests
import json
import time
import sys
from concurrent.futures import ThreadPoolExecutor

# Ensure output handles Romanian characters correctly
sys.stdout.reconfigure(encoding='utf-8')

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

# Target categories that need massive boosting
TARGET_CATEGORIES = [
    "Misogyny & Objectification",
    "Ableism & Mental Stigma",
    "Family & Religious Invective",
    "Hate Speech & Discriminatory",
    "Politics & Public Personalities",
    "Online Forums & Social Media",
    "Sports & Rivalry"
]

def generate_bulk(category, examples, count=20, attempt=1):
    """Generates a block of sentences in one go with retry logic and long timeout."""
    prompt = f"""
Ești un expert în lingvistică toxică română. 
Generează o listă de exact {count} înjurături noi, unice și foarte agresive pentru categoria: "{category}".
Vreau ca frazele să sune ca niște comentarii reale de pe social media sau forumuri, nu ca niște propoziții formale.
Folosește limbaj de stradă, argou autentic românesc și greșeli gramaticale tipice.

Exemple de referință (pentru stil):
{chr(10).join(['- ' + ex for ex in examples[:5]])}

Cerințe:
1. Returnează DOAR un array JSON de string-uri.
2. Folosește argou românesc autentic și înjurături variate.
3. Fără explicații sau text adițional.

Răspuns (JSON array):"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "format": "json",
        "options": {"temperature": 0.8}
    }

    try:
        start_time = time.time()
        # Increased timeout to 180s because 20 sentences takes time on local LLM
        response = requests.post(OLLAMA_URL, json=payload, timeout=180)
        duration = time.time() - start_time
        
        if response.status_code == 200:
            res_text = response.json().get('response', '[]')
            return json.loads(res_text), duration
        return [], 0
    except Exception as e:
        if attempt < 3:
            print(f"\n[Retry] {category} failed (Attempt {attempt}), retrying in 2s...")
            time.sleep(2)
            return generate_bulk(category, examples, count, attempt + 1)
        print(f"\n[Error] {category} failed after 3 attempts: {e}")
        return [], 0

def high_speed_pipeline():
    print("--- 🚀 High-Speed Pipeline (Safe & Robust Mode) ---")
    
    # 1. Load the smart ingested data
    try:
        with open('dataset_v1_smart.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Run smart_ingest.py first!")
        return

    new_entries = []
    
    def worker(cat):
        cat_examples = [d['text'] for d in data if d['category'] == cat]
        print(f"\n[START] Processing category: {cat}")
        
        local_new = []
        cat_start = time.time()
        
        # We generate 5 blocks of 20 = 100 new sentences per category
        for i in range(5):
            print(f"  [{cat}] Batch {i+1}/5 - Generating 20 sentences...", end="\r")
            batch, duration = generate_bulk(cat, cat_examples, count=20)
            
            if isinstance(batch, list) and len(batch) > 0:
                for text in batch:
                    local_new.append({"text": text, "category": cat})
                print(f"  [{cat}] Batch {i+1}/5 - Success! Added {len(batch)} items in {duration:.2f}s")
            else:
                print(f"  [{cat}] Batch {i+1}/5 - Failed to generate batch.")
            
            time.sleep(1) # Breathe between batches
            
        print(f"[FINISH] {cat} complete. Added {len(local_new)} items in {time.time() - cat_start:.2f}s")
        return local_new

    # SETTING max_workers=1 for stability. Local LLMs usually can't handle 
    # multiple parallel batch generations (especially 20 sentences each).
    with ThreadPoolExecutor(max_workers=1) as executor:
        results = list(executor.map(worker, TARGET_CATEGORIES))

    for res in results:
        new_entries.extend(res)

    # 3. Final Combine
    final_dataset = data + new_entries
    
    with open('dataset_final_balanced.json', 'w', encoding='utf-8') as f:
        json.dump(final_dataset, f, ensure_ascii=False, indent=2)

    print(f"\n--- Pipeline Finished ---")
    print(f"Original entries: {len(data)}")
    print(f"New synthetic entries: {len(new_entries)}")
    print(f"Final Dataset Size: {len(final_dataset)}")
    
    # Show balance
    counts = {}
    for d in final_dataset:
        counts[d['category']] = counts.get(d['category'], 0) + 1
    
    print("\nFinal Category Distribution:")
    for cat, count in counts.items():
        print(f" - {cat}: {count}")

if __name__ == "__main__":
    high_speed_pipeline()
