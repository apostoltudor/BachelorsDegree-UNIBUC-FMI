import json
import csv
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def clean_text(text):
    """
    Cleans the text by ensuring UTF-8 encoding and removing unnecessary whitespace.
    Preserves slang, misspellings, and slurs as per requirements.
    """
    if not text:
        return ""
    
    # Ensure text is treated as UTF-8 (Python 3 handles this by default for strings)
    # Remove excessive whitespace/newlines
    text = " ".join(text.split())
    
    return text

def placeholder_llm_classify(text, original_label):
    """
    Placeholder for future LLM-based re-classification.
    Currently uses rule-based mapping.
    """
    # Rule-based mapping
    mapping = {
        'ABUSE': 'General Aggression & Insults',
        'INSULT': 'General Aggression & Insults',
        'PROFANITY': 'General Aggression & Insults',
        'OTHER': 'General Aggression & Insults'  # Default for now
    }
    return mapping.get(original_label, 'General Aggression & Insults')

def load_phrases_json(file_path):
    """
    Loads data from phrases.json.
    """
    logging.info(f"Loading phrases from {file_path}")
    dataset = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for entry in data.get('data', []):
                category = entry.get('category')
                for sentence in entry.get('sentences', []):
                    dataset.append({
                        'text': clean_text(sentence),
                        'category': category
                    })
    except Exception as e:
        logging.error(f"Error loading {file_path}: {e}")
    return dataset

def load_csv_categories(dir_path):
    """
    Loads and harmonizes data from CSV files in the specified directory.
    """
    logging.info(f"Loading CSVs from {dir_path}")
    dataset = []
    csv_files = [f for f in os.listdir(dir_path) if f.endswith('.csv')]
    
    for filename in csv_files:
        file_path = os.path.join(dir_path, filename)
        logging.info(f"Processing {filename}")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    original_text = row.get('text', '')
                    original_label = row.get('label', '')
                    
                    # Harmonization step
                    harmonized_category = placeholder_llm_classify(original_text, original_label)
                    
                    dataset.append({
                        'text': clean_text(original_text),
                        'category': harmonized_category
                    })
        except Exception as e:
            logging.error(f"Error processing {filename}: {e}")
            
    return dataset

def main():
    base_dir = r'C:\Users\Cosmin\Documents\NLP'
    phrases_path = os.path.join(base_dir, 'phrases.json')
    csv_dir = os.path.join(base_dir, 'categorii_split')
    output_path = os.path.join(base_dir, 'dataset_v1.json')
    
    # 1. Load data from phrases.json
    phrases_data = load_phrases_json(phrases_path)
    logging.info(f"Loaded {len(phrases_data)} entries from phrases.json")
    
    # 2. Load data from CSVs
    csv_data = load_csv_categories(csv_dir)
    logging.info(f"Loaded {len(csv_data)} entries from CSV files")
    
    # 3. Combine datasets
    full_dataset = phrases_data + csv_data
    logging.info(f"Total entries in harmonized dataset: {len(full_dataset)}")
    
    # 4. Save to dataset_v1.json
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(full_dataset, f, ensure_ascii=False, indent=2)
        logging.info(f"Successfully saved harmonized dataset to {output_path}")
    except Exception as e:
        logging.error(f"Error saving output file: {e}")

if __name__ == "__main__":
    main()
