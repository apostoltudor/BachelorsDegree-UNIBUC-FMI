import os
import requests
import json
import time
from dotenv import load_dotenv

# Load the tokens from hf_pipeline/.env
load_dotenv(dotenv_path="hf_pipeline/.env")

# Dynamically gather all tokens that start with HF_TOKEN (e.g., HF_TOKEN, HF_TOKEN_2, HF_TOKEN_BACKUP)
tokens = []
for key, value in os.environ.items():
    if key.upper().startswith("HF_TOKEN") and value.strip():
        tokens.append(value.strip())

if not tokens:
    print("❌ No HF_TOKEN found in hf_pipeline/.env")
    exit(1)

print(f"✅ Found {len(tokens)} Hugging Face tokens for rotation.")
current_token_idx = 0

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
    "Family & Religious Invective",
    "Neutral"
]

def categorize_batch(texts):
    global current_token_idx
    
    prompt = f"""Clasifică următoarele {len(texts)} comentarii românești în una din aceste categorii:
{json.dumps(CATEGORIES, indent=2)}

Comentarii:
{json.dumps(texts, indent=2)}

Returnează DOAR un array JSON cu numele categoriei pentru fiecare comentariu, în ordine.
Ia in considerare si cuvantul gasit si categoria pusa deja.
Daca considerti ca un comentariu nu se încadreaza ca insulta, pune l ca "Neutral".
Exemplu: ["Politics & Public Personalities", "General Aggression & Insults"]"""

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "Ești un expert în clasificarea textelor toxice. Răspunzi doar cu JSON."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.1
    }

    attempts = 0
    max_attempts = len(tokens) * 2  # Allows us to cycle through all tokens at least twice before giving up
    
    while attempts < max_attempts:
        token = tokens[current_token_idx]
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(API_URL, headers=headers, json=payload, timeout=45)
            if response.status_code == 200:
                res_json = response.json()
                content = res_json['choices'][0]['message']['content']
                content = content.replace("```json", "").replace("```", "").strip()
                return json.loads(content)
            elif response.status_code in [429, 402, 503, 504]: # Rate limit, payment required, or server timeout/overload
                print(f"\n⚠️ Token {current_token_idx+1} received {response.status_code} (Rate Limit / Timeout). Switching token...")
                current_token_idx = (current_token_idx + 1) % len(tokens)
                attempts += 1
                time.sleep(2)  # Give it a short breath before retrying
            else:
                print(f"\n❌ Error {response.status_code}: {response.text}")
                return None
        except requests.exceptions.Timeout:
            print(f"\n⚠️ Request Timeout on token {current_token_idx+1}. Switching token...")
            current_token_idx = (current_token_idx + 1) % len(tokens)
            attempts += 1
            time.sleep(2)
        except Exception as e:
            print(f"\n❌ Exception: {e}")
            return None
            
    print("\n❌ All tokens depleted or failed. Batch skipped.")
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
            print(f"\n  Batch failed at {i}. Retrying with smaller chunks...")
            time.sleep(3)
            # Second attempt item by item
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

        # Save progress continually
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(classified_data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Finished {output_path}. Saved {len(classified_data)} items.")

def main():
    # Process the aggregated data
    process_file('reddit_scraper/categorized_csv_data.json', 'reddit_scraper/double_checked_csv_data.json')
   
if __name__ == "__main__":
    main()
