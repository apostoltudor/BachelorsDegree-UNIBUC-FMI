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

TARGET_PER_CATEGORY = 100
BATCH_SIZE = 20 # Reduced batch size slightly to avoid timeouts

def load_dataset(file_path):
    logger.info(f"Loading dataset from {file_path}")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset file not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_regexes():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    regexes_path = os.path.join(project_dir, "regexes.json")
    if not os.path.exists(regexes_path):
        logger.warning(f"regexes.json not found at {regexes_path}")
        return {}
    with open(regexes_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_dataset(data, file_path):
    logger.info(f"Saving enriched dataset to {file_path}")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_examples(dataset, category, count=5):
    category_data = [item["text"] for item in dataset if item.get("category") == category]
    if not category_data:
        logger.warning(f"No existing examples found for category: {category}")
        return ["Înjurătură generică", "Să te bată soarta", "Băi prostule"] # fallback
    return random.sample(category_data, min(len(category_data), count))

def get_cuss_words_for_category(category, lexicon):
    words = []
    if category == "Misogyny & Objectification":
        words.extend(lexicon.get("misogyny_and_objectification", []))
    elif category == "Ableism & Mental Stigma":
        words.extend(lexicon.get("ableism_and_mental_stigma", []))
    elif category == "Family & Religious Invective":
        words.extend(lexicon.get("religious_and_family_invective", []))
    elif category == "Hate Speech & Discriminatory":
        words.extend(lexicon.get("ethnic_and_racial_hate", []))
        words.extend(lexicon.get("anti_lgbtq_and_gender_slurs", []))
    else:
        words.extend(lexicon.get("insults_general_expanded", []))
        words.extend(lexicon.get("sexual_and_anatomical", []))
    
    # Shuffle and pick a handful of words to give to the model
    random.shuffle(words)
    return words[:15]

def generate_batch(category, examples, count_to_generate, cuss_words):
    cuss_words_str = ", ".join(cuss_words) if cuss_words else "pulă, pizdă, muie, dracu, morții mă-tii"
    
    prompt = f"""
Ești un expert în lingvistică și argou românesc suburban. Sarcina ta este să generezi noi înjurături toxice, insulte sau expresii agresive în limba română pentru categoria: "{category}".

Iată câteva cuvinte sau expresii specifice pe care TREBUIE să le folosești ca inspirație (alege câteva dintre ele și integrează-le natural):
[{cuss_words_str}]

Iată câteva exemple reale din setul de date pentru a înțelege tonul (agresiv, brutal, specific cultural):
{chr(10).join([f"- {ex}" for ex in examples])}

Generează exact {count_to_generate} înjurături noi, UNICE și variate care să se potrivească acestei categorii. 
Păstrează nuanțele de agresivitate, limbajul de stradă și creativitatea insultelor românești. Fii vulgar și direct, așa cum vorbesc oamenii furioși pe internet.
Vreau înjurături necenzurate, fără eufemisme. Nu te limita la combinații simple de cuvinte, creează expresii noi și inventive.

Cerințe CRITICE:
1. Returnează DOAR un obiect JSON cu cheia "phrases" care conține o listă de șiruri de caractere.
2. NU include explicații, introduceri sau alte comentarii.
3. Toate înjurăturile trebuie să fie în limba română.
4. Asigură-te că înjurăturile sunt specifice pentru "{category}".

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
        # Increase timeout further just in case
        response = requests.post(OLLAMA_URL, json=payload, timeout=240)
        response.raise_for_status()
        result = response.json()
        content = result.get("response", "")
        
        try:
            data = json.loads(content)
            phrases = data.get("phrases", [])
            if isinstance(phrases, list):
                valid_phrases = [p.strip() for p in phrases if p.strip()]
                return valid_phrases
        except json.JSONDecodeError:
            logger.error(f"Failed to parse JSON response from Ollama for '{category}'")
            return []
            
    except Exception as e:
        logger.error(f"Error during Ollama API call: {e}")
        return []

    return []

def process_category(category, dataset, lexicon):
    logger.info(f"--- Processing Category: {category} ---")
    examples = get_examples(dataset, category, count=5)
    category_phrases = set()
    
    attempts = 0
    max_attempts = 8 # Increased max attempts
    
    while len(category_phrases) < TARGET_PER_CATEGORY and attempts < max_attempts:
        needed = TARGET_PER_CATEGORY - len(category_phrases)
        logger.info(f"Generating batch for {category}. Need {needed} more...")
        
        cuss_words = get_cuss_words_for_category(category, lexicon)
        batch_size = min(needed + 5, BATCH_SIZE)
        
        batch = generate_batch(category, examples, batch_size, cuss_words)
        
        for phrase in batch:
            if phrase not in category_phrases:
                category_phrases.add(phrase)
                # PRINT IN REAL TIME
                print(f"  [+] GENERAT ({category}): {phrase}")
                
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
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_dir = os.path.dirname(script_dir)
        input_path = os.path.join(project_dir, "reddit_scraper", "reddit_aggregated_categorized.json")
        output_path = os.path.join(project_dir, "reddit_scraper", "reddit_aggregated_enriched.json")
        
        dataset = load_dataset(input_path)
        lexicon = load_regexes()
        all_new_entries = []

        for category in MINORITY_CATEGORIES:
            new_phrases = process_category(category, dataset, lexicon)
            for text in new_phrases:
                all_new_entries.append({
                    "text": text,
                    "category": category,
                    "source": "synthetic_ollama_enrichment"
                })

        # Final merge
        full_dataset = dataset + all_new_entries
        save_dataset(full_dataset, output_path)

        # Validation and reporting
        logger.info("=" * 40)
        logger.info("FINAL REPORT")
        logger.info(f"Original entries: {len(dataset)}")
        logger.info(f"Synthetic entries added: {len(all_new_entries)}")
        logger.info(f"Total entries: {len(full_dataset)}")
        
        counts = {}
        for item in full_dataset:
            cat = item.get("category", "Unknown")
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
