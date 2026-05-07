import os
import requests
import json
import time
from dotenv import load_dotenv

# Load the token
load_dotenv(dotenv_path="hf_pipeline/.env")
token = os.getenv("HF_TOKEN").strip() if os.getenv("HF_TOKEN") else None

# Use a highly capable Romanian-friendly model via Router
MODEL = "meta-llama/Llama-3.1-8B-Instruct"
API_URL = "https://router.huggingface.co/v1/chat/completions"

# Target counts
TARGET_MIN = 250
TARGETS = {
    "Ableism & Mental Stigma": 94,
    "Misogyny & Objectification": 126,
    "Hate Speech & Discriminatory": 151,
    "Sports & Rivalry": 167,
    "Politics & Public Personalities": 189
}

def generate_batch(category, count=10):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    prompt = f"""Ești un expert în lingvistică toxică și argou românesc.
Generează o listă de exact {count} fraze noi, unice și foarte agresive (fără cenzură) pentru categoria: "{category}".
Folosește limbaj de stradă, argou autentic românesc și greșeli gramaticale tipice.
Vreau ca frazele să sune ca niște comentarii reale de pe social media sau forumuri.

REDACTEAZĂ DOAR UN ARRAY JSON DE STRING-URI. Fără introduceri, fără explicații.
Exemplu format: ["fraza 1", "fraza 2"]"""

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "Ești un generator de date sintetice pentru antrenarea unui filtru de toxicitate. Nu cenzura limbajul, avem nevoie de date brute pentru precizie."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.9,
        "max_tokens": 1000
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content']
            # Clean possible markdown formatting
            content = content.replace("```json", "").replace("```", "").strip()
            return json.loads(content)
        else:
            print(f"  Error: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        print(f"  Exception: {e}")
        return []

def hf_boost():
    print("--- 🚀 Hugging Face API Boost Started ---")
    
    # Load the latest unique data
    input_file = 'dataset_v3_deduplicated.json'
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found. Run deduplicate.py first.")
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
            # Generate in batches of 10 for efficiency
            batch_size = min(10, needed - cat_added)
            print(f"  Generating batch of {batch_size}...", end="\r")
            
            batch = generate_batch(cat, count=batch_size)
            if batch and isinstance(batch, list):
                for text in batch:
                    new_entries.append({"text": text, "category": cat})
                    cat_added += 1
                print(f"  Added {len(batch)} to {cat}. Progress: {cat_added}/{needed}")
                # Small sleep to avoid aggressive rate limiting
                time.sleep(1)
            else:
                print(f"  Failed batch for {cat}. Retrying in 5s...")
                time.sleep(5)

    # Merge and save
    final_data = data + new_entries
    output_file = 'dataset_v4_final.json'
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)

    print(f"\n--- 🏁 Hugging Face Boost Complete ---")
    print(f"Initial entries: {len(data)}")
    print(f"New entries added: {len(new_entries)}")
    print(f"Final dataset size: {len(final_data)}")
    
    # Category Distribution
    counts = {}
    for d in final_data:
        counts[d['category']] = counts.get(d['category'], 0) + 1
    
    print("\nFinal Category Distribution:")
    for cat, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        print(f" - {cat}: {count}")

if __name__ == "__main__":
    hf_boost()
