import json
import requests
import time
import logging
import random
import sys
import os

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

MINORITY_CATEGORIES = [
    "Misogyny & Objectification",
    "Ableism & Mental Stigma",
    "Family & Religious Invective",
    "Hate Speech & Discriminatory",
    "Politics & Public Personalities",
    "Online Forums & Social Media",
    "Sports & Rivalry"
]

TARGET_PER_CATEGORY = 50
BATCH_SIZE = 25 # We'll try to get 25 at a time to be safe and efficient

def load_dataset(file_path):
    logger.info(f"Loading dataset from {file_path}")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset file not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_dataset(data, file_path):
    logger.info(f"Saving enriched dataset to {file_path}")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_examples(dataset, category, count=5):
    category_data = [item["text"] for item in dataset if item["category"] == category]
    if not category_data:
        logger.warning(f"No existing examples found for category: {category}")
        return []
    return random.sample(category_data, min(len(category_data), count))

def generate_batch(category, examples, count_to_generate):
    prompt = f"""
Ești un expert în lingvistică și argou românesc suburban. Sarcina ta este să generezi noi fraze toxice, insulte sau expresii agresive în limba română pentru categoria: "{category}".

Iată câteva exemple reale din setul de date pentru a înțelege tonul (agresiv, brutal, specific cultural):
{chr(10).join([f"- {ex}" for ex in examples])}

Generează exact {count_to_generate} fraze noi, UNICE și variate care să se potrivească acestei categorii. 
Păstrează nuanțele de agresivitate, limbajul de stradă și creativitatea insultelor românești.

Cerințe CRITICE:
1. Returnează DOAR un obiect JSON cu cheia "phrases" care conține o listă de șiruri de caractere.
2. NU include explicații, introduceri sau alte comentarii.
3. Toate frazele trebuie să fie în limba română.
4. Asigură-te că frazele sunt specifice pentru "{category}".

Format output:
{{
  "phrases": ["frază 1", "frază 2", ...]
}}
"""
    
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "format": "json"
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=180)
        response.raise_for_status()
        result = response.json()
        content = result.get("response", "")
        
        try:
            data = json.loads(content)
            phrases = data.get("phrases", [])
            if isinstance(phrases, list):
                return [p.strip() for p in phrases if p.strip()]
        except json.JSONDecodeError:
            logger.error(f"Failed to parse JSON response from Ollama for '{category}'")
            return []
            
    except Exception as e:
        logger.error(f"Error during Ollama API call: {e}")
        return []

    return []

def process_category(category, dataset):
    logger.info(f"--- Processing Category: {category} ---")
    examples = get_examples(dataset, category, count=5)
    category_phrases = set()
    
    # We want exactly TARGET_PER_CATEGORY
    attempts = 0
    max_attempts = 5
    
    while len(category_phrases) < TARGET_PER_CATEGORY and attempts < max_attempts:
        needed = TARGET_PER_CATEGORY - len(category_phrases)
        logger.info(f"Generating batch for {category}. Need {needed} more...")
        
        batch = generate_batch(category, examples, min(needed + 5, BATCH_SIZE))
        for phrase in batch:
            if phrase not in category_phrases:
                category_phrases.add(phrase)
            if len(category_phrases) >= TARGET_PER_CATEGORY:
                break
        
        attempts += 1
        if len(category_phrases) < TARGET_PER_CATEGORY:
            time.sleep(2) # Brief pause between retries
            
    logger.info(f"Completed {category}: {len(category_phrases)} phrases generated.")
    return list(category_phrases)

def main():
    start_time = time.time()
    try:
        dataset = load_dataset("dataset_v1.json")
        all_new_entries = []

        for category in MINORITY_CATEGORIES:
            new_phrases = process_category(category, dataset)
            for text in new_phrases:
                all_new_entries.append({
                    "text": text,
                    "category": category
                })

        # Final merge
        full_dataset = dataset + all_new_entries
        save_dataset(full_dataset, "dataset_v2_synthetic.json")

        # Validation and reporting
        logger.info("=" * 40)
        logger.info("FINAL REPORT")
        logger.info(f"Original entries: {len(dataset)}")
        logger.info(f"Synthetic entries added: {len(all_new_entries)}")
        logger.info(f"Total entries: {len(full_dataset)}")
        
        counts = {}
        for item in full_dataset:
            cat = item["category"]
            counts[cat] = counts.get(cat, 0) + 1
        
        logger.info("Per-category distribution:")
        for cat in sorted(counts.keys()):
            logger.info(f"- {cat}: {counts[cat]}")
        
        duration = time.time() - start_time
        logger.info(f"Total execution time: {duration:.2f} seconds")

    except Exception as e:
        logger.exception(f"Fatal error during execution: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
