import json
import pandas as pd
import glob
import os

def smart_ingest():
    # 1. Load initial seeds
    with open('phrases.json', 'r', encoding='utf-8') as f:
        seeds = json.load(f)['data']
    
    final_data = []
    for category_group in seeds:
        cat_name = category_group['category']
        for sentence in category_group['sentences']:
            final_data.append({"text": sentence, "category": cat_name})
            
    # 2. Map CSVs to specific categories instead of "General"
    # Mapping based on filename and content hints
    csv_mapping = {
        "categoria_ABUSE.csv": "General Aggression & Insults",
        "categoria_INSULT.csv": "General Aggression & Insults",
        "categoria_PROFANITY.csv": "Family & Religious Invective", # Romanian profanity is often religious/family based
        "categoria_OTHER.csv": "Online Forums & Social Media"
    }
    
    for csv_file in glob.glob('categorii_split/*.csv'):
        filename = os.path.basename(csv_file)
        target_cat = csv_mapping.get(filename, "General Aggression & Insults")
        
        df = pd.read_csv(csv_file)
        # Clean: remove duplicates and short/empty text
        texts = df['text'].dropna().unique()
        
        for t in texts:
            if len(str(t)) > 5: # Skip garbage
                final_data.append({"text": str(t), "category": target_cat})
                
    with open('dataset_v1_smart.json', 'w', encoding='utf-8') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)
    
    print(f"Smart Ingestion Complete. Total: {len(final_data)}")

if __name__ == "__main__":
    smart_ingest()
