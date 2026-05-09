import os
import json
from collections import defaultdict
import matplotlib.pyplot as plt

# ==========================================
# CONFIGURAȚIE
# Adaugă aici numele fișierelor JSON pe care vrei să le analizezi.
# Asigură-te că fișierele sunt în același folder cu acest script, sau pune calea completă.
# ==========================================
JSON_FILES = [
    "reddit_aggregated_categorized.json",
    "categorized_news_ro_data.json",
    "categorized_ro_fb_data.json",
    "categorized_reddit_data.json",
    "categorized_roff_data.json",
    "reddit_aggregated_enriched.json",
]

def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Eroare la citirea {filepath}: {e}")
        return []

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Structuri pentru stocarea datelor
    # stats_per_file[filename]['categories'][category] = count
    # stats_per_file[filename]['sources'][source] = count
    stats_per_file = defaultdict(lambda: {'categories': defaultdict(int), 'sources': defaultdict(int)})
    
    for filename in JSON_FILES:
        filepath = os.path.join(script_dir, filename)
        if not os.path.exists(filepath):
            print(f"Avertisment: Fișierul '{filename}' nu a fost găsit la {filepath}. Se omite.")
            continue
            
        print(f"Procesez {filename}...")
        data = load_data(filepath)
        
        for item in data:
            cat = item.get("category", "Necunoscut")
            # Unele fișiere ar putea avea 'macro_source', altele 'source'
            src = item.get("macro_source", item.get("source", "Necunoscut"))
            
            stats_per_file[filename]['categories'][cat] += 1
            stats_per_file[filename]['sources'][src] += 1
            
    # Afișare statistici în consolă și generare grafice
    for filename, stats in stats_per_file.items():
        print(f"\n{'='*50}")
        print(f"📊 STATISTICI PENTRU: {filename}")
        print(f"{'='*50}")
        
        categories = dict(sorted(stats['categories'].items(), key=lambda x: x[1], reverse=True))
        sources = dict(sorted(stats['sources'].items(), key=lambda x: x[1], reverse=True))
        
        print("\nCategorii:")
        for cat, count in categories.items():
            print(f"  - {cat}: {count}")
            
        print("\nSurse:")
        for src, count in sources.items():
            print(f"  - {src}: {count}")
            
        # --- Generare Histogramă Categorii ---
        if categories:
            plt.figure(figsize=(14, 7))
            bars = plt.bar(categories.keys(), categories.values(), color='skyblue', edgecolor='black')
            plt.title(f'Distribuția Categoriilor - {filename}', fontsize=16)
            plt.xlabel('Categorie', fontsize=12)
            plt.ylabel('Număr de comentarii', fontsize=12)
            plt.xticks(rotation=45, ha='right', fontsize=10)
            
            # Adăugare valori pe bare
            for bar in bars:
                yval = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2, yval + (max(categories.values()) * 0.01), int(yval), ha='center', va='bottom', fontsize=10)
                
            plt.tight_layout()
            output_img = os.path.join(script_dir, f"hist_categories_{filename.replace('.json', '.png')}")
            plt.savefig(output_img, dpi=300)
            print(f"\nGraficul pentru categorii a fost salvat ca: {os.path.basename(output_img)}")
            plt.close()
            
        # --- Generare Histogramă Surse ---
        if sources:
            plt.figure(figsize=(14, 7))
            bars = plt.bar(sources.keys(), sources.values(), color='lightcoral', edgecolor='black')
            plt.title(f'Distribuția Surselor - {filename}', fontsize=16)
            plt.xlabel('Sursă', fontsize=12)
            plt.ylabel('Număr de comentarii', fontsize=12)
            plt.xticks(rotation=45, ha='right', fontsize=10)
            
            for bar in bars:
                yval = bar.get_height()
                plt.text(bar.get_x() + bar.get_width()/2, yval + (max(sources.values()) * 0.01), int(yval), ha='center', va='bottom', fontsize=10)
                
            plt.tight_layout()
            output_img = os.path.join(script_dir, f"hist_sources_{filename.replace('.json', '.png')}")
            plt.savefig(output_img, dpi=300)
            print(f"Graficul pentru surse a fost salvat ca: {os.path.basename(output_img)}")
            plt.close()

if __name__ == "__main__":
    main()
