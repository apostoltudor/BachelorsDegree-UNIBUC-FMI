import os
import json
import glob
from collections import defaultdict

def aggregate_and_stats():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    search_pattern = os.path.join(script_dir, "**", "categorized_*_data.json")
    all_files = glob.glob(search_pattern, recursive=True)
    
    # Ignore files in 'categorized_files' directory
    files = [f for f in all_files if "categorized_files" not in f.replace("\\", "/")]
    
    if not files:
        print(f"Nu am găsit fișiere 'categorized_*_data.json' valide în directorul {script_dir}")
        return

    all_data = []
    
    # We want to group by these 4 macro-sources
    # stats[macro_source][category] = count
    stats = defaultdict(lambda: defaultdict(int))
    category_totals = defaultdict(int)
    macro_source_totals = defaultdict(int)
    
    print("--- Agregare Date ---")
    for filepath in files:
        filename = os.path.basename(filepath)
        print(f"Citesc: {filename}")
        
        # Determine macro source based on filename
        if filename == "categorized_news_ro_data.json":
            macro_source = "news_ro"
        elif filename == "categorized_ro_fb_data.json":
            macro_source = "ro_fb"
        elif filename == "categorized_roff_data.json":
            macro_source = "roff"
        else:
            macro_source = "reddit_data"
            
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            for item in data:
                # Optional: update the source in the final JSON to reflect the macro group
                item["macro_source"] = macro_source
                all_data.append(item)
                
                category = item.get("category", "Unknown")
                
                stats[macro_source][category] += 1
                category_totals[category] += 1
                macro_source_totals[macro_source] += 1
                
        except Exception as e:
            print(f"Eroare la citirea {filename}: {e}")

    # Save to a single file
    output_file = os.path.join(script_dir, "reddit_aggregated_categorized.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
        
    print(f"\n✅ S-au combinat {len(all_data)} comentarii într-un singur fișier:")
    print(f"💾 Salvat în: {output_file}")
    
    print("\n" + "="*50)
    print("📊 STATISTICI: CATEGORII PER SURSĂ PRINCIPALĂ")
    print("="*50)
    
    for source, cat_counts in sorted(stats.items()):
        print(f"\n📍 Sursă: {source} (Total: {macro_source_totals[source]})")
        for cat, count in sorted(cat_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"    - {cat}: {count}")
            
    print("\n" + "="*50)
    print("📈 TOTALURI PE CATEGORII (Toate sursele)")
    print("="*50)
    for cat, count in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
        print(f"  🔥 {cat}: {count}")

if __name__ == "__main__":
    aggregate_and_stats()
