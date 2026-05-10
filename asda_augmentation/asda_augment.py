import os
import json
import random
import requests
import time
import logging
import sys

# Configure structured logging to see real-time outputs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

# Probability to mask a word in E2
MASK_PROBABILITY = 0.25

def load_dataset(file_path):
    if not os.path.exists(file_path):
        logger.error(f"Fișierul nu a fost găsit: {file_path}")
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def mask_sentence(text, prob=0.25):
    """
    Randomly masks words in a sentence based on the probability.
    """
    words = text.split()
    if len(words) <= 3:
        # If the sentence is too short, just mask one random word (if possible)
        if words:
            idx = random.randint(0, len(words) - 1)
            words[idx] = "[MASK]"
        return " ".join(words)
        
    masked_words = []
    masks_applied = 0
    for word in words:
        if random.random() < prob:
            masked_words.append("[MASK]")
            masks_applied += 1
        else:
            masked_words.append(word)
            
    # Ensure at least one mask is applied if length > 3
    if masks_applied == 0:
        idx = random.randint(0, len(words) - 1)
        masked_words[idx] = "[MASK]"
        
    return " ".join(masked_words)

def generate_asda_example(category, e1_text, e2_masked):
    """
    Calls Ollama to reconstruct E2 given the ASDA context.
    """
    prompt = f"""
Ești un asistent AI expert în procesarea limbajului natural în limba română.
Sarcina ta este să completezi cuvintele lipsă (marcate cu [MASK]) dintr-o propoziție, folosind un context.

Context:
"Următoarele două propoziții fac parte din categoria: {category} (limbaj agresiv/toxic). 
Prima propoziție este: {e1_text}. 
A doua propoziție este: {e2_masked}."

Completează cuvintele [MASK] cu termeni potriviți care respectă tonul, argoul și nivelul de toxicitate al categoriei "{category}".
Regulă CRITICĂ: Răspunde DOAR cu a doua propoziție completată, sub formă de text curat. Fără ghilimele, fără explicații suplimentare.
"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        if response.status_code == 200:
            result = response.json()
            return result.get("response", "").strip()
        else:
            logger.error(f"Ollama a returnat eroarea: {response.status_code}")
            return None
    except Exception as e:
        logger.error(f"Eroare de conexiune cu Ollama: {e}")
        return None

def run_asda_augmentation(dataset_path, output_path, samples_per_category=20):
    logger.info("Încărcare dataset...")
    dataset = load_dataset(dataset_path)
    if not dataset:
        return
        
    # Group by category
    categorized_data = {}
    for item in dataset:
        cat = item.get("category", "Unknown")
        if cat not in categorized_data:
            categorized_data[cat] = []
        categorized_data[cat].append(item["text"])
        
    augmented_data = []
    
    logger.info(f"Începem ASDA (Auxiliary Sentence-based Data Augmentation) - {samples_per_category} per categorie\n")
    
    for category, texts in categorized_data.items():
        if len(texts) < 2:
            logger.warning(f"Nu există suficiente texte în categoria '{category}' pentru a aplica ASDA.")
            continue
            
        logger.info(f"{'='*60}")
        logger.info(f"📁 Categoria: {category} (Total disponibile: {len(texts)})")
        logger.info(f"{'='*60}")
        
        successful_samples = 0
        attempts = 0
        
        while successful_samples < samples_per_category and attempts < samples_per_category * 3:
            attempts += 1
            
            # 1. Select E1 and E2
            e1, e2 = random.sample(texts, 2)
            
            # 2. Mask E2
            e2_masked = mask_sentence(e2, MASK_PROBABILITY)
            
            # Skip if masking didn't change anything (edge case)
            if "[MASK]" not in e2_masked:
                continue
                
            # 3. Print Logs before generation
            logger.info(f"--- Generare {successful_samples + 1}/{samples_per_category} ---")
            logger.info(f"E1 (Context) : {e1}")
            logger.info(f"E2 (Original): {e2}")
            logger.info(f"E2 (Mascat)  : {e2_masked}")
            
            # 4. Call LLM
            e2_generated = generate_asda_example(category, e1, e2_masked)
            
            if e2_generated:
                # Clean up response just in case the LLM was chatty
                e2_generated = e2_generated.replace('"', '').strip()
                
                logger.info(f"E2 (ASDA Gen): {e2_generated}")
                
                augmented_data.append({
                    "text": e2_generated,
                    "category": category,
                    "source": "asda_augmentation",
                    "original_e1": e1,
                    "original_e2": e2
                })
                successful_samples += 1
            else:
                logger.warning("Generarea a eșuat. Se reîncearcă...")
                
            time.sleep(1) # Scurtă pauză pentru a nu supraîncărca LLM-ul
            
    # Save the new ASDA generated items
    logger.info(f"\nSalvare a {len(augmented_data)} exemple ASDA noi în {output_path}")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(augmented_data, f, ensure_ascii=False, indent=2)
        
    logger.info("✅ ASDA Augmentation finalizată cu succes!")

if __name__ == "__main__":
    # Căile către fișiere
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    
    # Folosim dataset-ul pe care l-am agregat anterior
    INPUT_JSON = os.path.join(project_dir, "reddit_scraper", "reddit_aggregated_categorized.json")
    OUTPUT_JSON = os.path.join(script_dir, "asda_generated_data.json")
    
    # Rulează scriptul
    run_asda_augmentation(INPUT_JSON, OUTPUT_JSON, samples_per_category=5)
