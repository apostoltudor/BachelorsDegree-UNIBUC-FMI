import requests
import json
import time
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

# Target counts for minority categories
TARGET_MIN = 250
TARGETS = {
    "Ableism & Mental Stigma": 94,
    "Misogyny & Objectification": 126,
    "Hate Speech & Discriminatory": 151,
    "Sports & Rivalry": 167,
    "Politics & Public Personalities": 189
}

def generate_small_batch(category, count=5, attempt=1):
    prompt = f"""Ești un expert în lingvistică toxică română. 
Generează o listă de exact {count} fraze noi, unice și foarte agresive pentru categoria: "{category}".
Folosește argou autentic.
Returnează DOAR un array JSON de string-uri. Fără explicații."""

    payload = {
        "model": MODEL, 
        "prompt": prompt, 
        "stream": False, 
        "format": "json",
        "options": {"temperature": 0.8}
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=90)
        if response.status_code == 200:
            res_text = response.json().get('response', '[]')
            return json.loads(res_text)
        return []
    except Exception as e:
        if attempt < 3:
            time.sleep(2)
            return generate_small_batch(category, count, attempt + 1)
        return []

def final_boost():
    print("--- 🚀 Final Targeted Boost Started ---")
    
    input_file = 'dataset_v3_deduplicated.json'
    if not os.path.exists(input_file):
        print("Run deduplicate.py first!")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    new_entries = []
    
    for cat, current_count in TARGETS.items():
        needed = TARGET_MIN - current_count
        if needed <= 0:
            continue
            
        print(f"\n[Target] {cat}: Need {needed} more...")
        
        cat_added = 0
        while cat_added < needed:
            # Generate in small batches of 5 for stability
            batch_size = min(5, needed - cat_added)
            print(f"  Generating batch ({cat_added}/{needed})...", end="\r")
            
            batch = generate_small_batch(cat, count=batch_size)
            if batch and isinstance(batch, list):
                for text in batch:
                    new_entries.append({"text": text, "category": cat})
                    cat_added += 1
                print(f"  Added {len(batch)} to {cat}. Total added: {cat_added}")
            else:
                print(f"  Failed batch. Retrying...")
                time.sleep(1)

    # Final merge and save
    final_data = data + new_entries
    output_file = 'dataset_v4_final.json'
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)

    print(f"\n--- Boost Complete ---")
    print(f"New entries added: {len(new_entries)}")
    
    # Final check
    counts = {}
    for d in final_data:
        counts[d['category']] = counts.get(d['category'], 0) + 1
    
    print("\nFinal Balanced Distribution:")
    for cat, count in sorted(counts.items(), key=lambda x: x[1]):
        print(f" - {cat}: {count}")

if __name__ == "__main__":
    final_boost()
