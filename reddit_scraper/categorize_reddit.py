import os
import requests
import json
import time
from dotenv import load_dotenv

# Load the token from hf_pipeline/.env
load_dotenv(dotenv_path="hf_pipeline/.env")
token = os.getenv("HF_TOKEN").strip() if os.getenv("HF_TOKEN") else None

MODEL = "meta-llama/Llama-3.1-8B-Instruct"
API_URL = "https://router.huggingface.co/v1/chat/completions"

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

def categorize_batch(texts):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # We ask for a list of categories in order
    prompt = f"""Clasifică următoarele {len(texts)} comentarii românești în una din aceste categorii:
{json.dumps(CATEGORIES, indent=2)}

Comentarii:
{json.dumps(texts, indent=2)}

Returnează DOAR un array JSON cu numele categoriei pentru fiecare comentariu, în ordine.
Exemplu: ["Politics & Public Personalities", "General Aggression & Insults"]"""

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "Ești un expert în clasificarea textelor toxice. Răspunzi doar cu JSON."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.1
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        if response.status_code == 200:
            res_json = response.json()
            content = res_json['choices'][0]['message']['content']
            content = content.replace("```json", "").replace("```", "").strip()
            return json.loads(content)
        elif response.status_code == 402:
            print("\n❌ Credits depleted on HF. Try a different token or wait.")
            return None
        else:
            print(f"\n❌ Error {response.status_code}: {response.text}")
            return None
    except Exception as e:
        print(f"\n❌ Exception: {e}")
        return None

def process_file(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"\nProcessing {input_path} ({len(data)} items)...")
    
    classified_data = []
    batch_size = 10
    
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]
        texts = [item['text'] for item in batch]
        
        print(f"  Categorizing {i}/{len(data)}...", end="\r")
        
        labels = categorize_batch(texts)
        if labels and isinstance(labels, list) and len(labels) == len(batch):
            for item, label in zip(batch, labels):
                classified_data.append({
                    "text": item['text'],
                    "category": label if label in CATEGORIES else "General Aggression & Insults",
                    "source": item.get('source', 'reddit')
                })
        else:
            print(f"\n  Batch failed at {i}. Retrying in 5s...")
            time.sleep(5)
            # Second attempt with smaller batch
            for item in batch:
                label_list = categorize_batch([item['text']])
                if label_list and len(label_list) > 0:
                    label = label_list[0]
                    classified_data.append({
                        "text": item['text'],
                        "category": label if label in CATEGORIES else "General Aggression & Insults",
                        "source": item.get('source', 'reddit')
                    })
                time.sleep(1)

        # Save progress
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(classified_data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Finished {output_path}. Saved {len(classified_data)} items.")

def main():
    # 1. Romania
    process_file('reddit_scraper/scraped_reddit_data.json', 'reddit_scraper/classified_romania.json')
    # 2. Roumanie
    process_file('reddit_scraper/scraped_roumanie_data.json', 'reddit_scraper/classified_roumanie.json')

if __name__ == "__main__":
    main()
