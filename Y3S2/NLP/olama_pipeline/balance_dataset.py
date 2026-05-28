import os
import json
import random
from collections import defaultdict

# ==========================================
# CONFIGURAȚIE
# ==========================================
# Calea către dataset-ul tău masiv (ex: aggregated sau un dataset existent)
INPUT_FILE = r"C:\Users\Cosmin\Documents\NLP\reddit_scraper\reddit_aggregated_enriched.json"

# Numele fișierului echilibrat pe care vrei să-l creezi (ex: dataset_v6_balanced.json)
OUTPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "dataset_v7    _balanced.json")

# Limita maximă de comentarii per categorie.
# Dacă o categorie are mai mult de MAX_PER_CATEGORY, va fi redusă aleatoriu (downsampling) la acest număr.
# Dacă are mai puțin, vor fi păstrate toate.
# Ajustează acest număr în funcție de câte date vrei în total.
MAX_PER_CATEGORY = 400

def load_data(filepath):
    if not os.path.exists(filepath):
        print(f"Eroare: Nu s-a găsit fișierul {filepath}")
        return []
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def balance_dataset():
    print(f"--- ⚖️ Echilibrare Dataset ---")
    print(f"Citește din: {INPUT_FILE}")
    print(f"Limita per categorie: {MAX_PER_CATEGORY}")
    
    data = load_data(INPUT_FILE)
    if not data:
        return
        
    # Grupăm datele pe categorii
    categorized_data = defaultdict(list)
    for item in data:
        # Normalizare categorie dacă e necesar
        cat = item.get("category", "Unknown")
        
        # Eliminăm categoria Online Forums & Social Media
        if cat == "Online Forums & Social Media":
            continue
            
        categorized_data[cat].append(item)
        
    print("\n📊 Distribuția ORIGINALĂ:")
    for cat, items in sorted(categorized_data.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"  - {cat}: {len(items)}")

    balanced_data = []
    
    # Aplicăm downsampling
    for cat, items in categorized_data.items():
        if len(items) > MAX_PER_CATEGORY:
            # Alegem aleatoriu un eșantion dacă sunt prea multe
            sampled_items = random.sample(items, MAX_PER_CATEGORY)
            balanced_data.extend(sampled_items)
        else:
            # Dacă sunt mai puține sau egale cu limita, le păstrăm pe toate
            balanced_data.extend(items)
            
    # Amestecăm dataset-ul final pentru ca modelele de ML să nu primească datele ordonate pe categorii
    random.shuffle(balanced_data)
    
    print("\n📊 Distribuția ECHILIBRATĂ (Noul Dataset):")
    final_counts = defaultdict(int)
    for item in balanced_data:
        final_counts[item["category"]] += 1
        
    for cat, count in sorted(final_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  - {cat}: {count}")
        
    print(f"\nTotal comentarii în dataset-ul original: {len(data)}")
    print(f"Total comentarii în dataset-ul echilibrat: {len(balanced_data)}")
    
    # Salvare fișier
    save_data(balanced_data, OUTPUT_FILE)
    print(f"\n💾 Dataset-ul echilibrat a fost salvat în: {OUTPUT_FILE}")

if __name__ == "__main__":
    balance_dataset()
