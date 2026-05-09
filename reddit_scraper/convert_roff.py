import os
import csv
import json

def convert_roff():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    tsv_path = os.path.join(project_dir, 'ROFF-master', 'OLID_ROFF.tsv')
    
    if not os.path.exists(tsv_path):
        print(f"File not found: {tsv_path}")
        return

    all_data = []
    
    print(f"--- 🔄 Mapare Directă ROFF TSV în JSON ---")
    
    try:
        with open(tsv_path, 'r', encoding='utf-8') as f:
            # ROFF is a TSV, so we use tab as delimiter
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                text = row.get('Tweet', '').strip()
                label = row.get('Offensive', '').strip()
                
                if label == 'NOT':
                    category = "Neutral"
                elif label == 'OFF':
                    category = "General Aggression & Insults"
                else:
                    category = "Neutral"  # Fallback
                
                if text:
                    all_data.append({
                        "text": text,
                        "category": category,
                        "source": "csv/roff"
                    })
    except Exception as e:
        print(f"Eroare la citirea {tsv_path}: {e}")

    # Output directly to categorized_ to bypass check_offensive.py
    output_file = os.path.join(script_dir, "categorized_roff_data.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
        
    print(f"\n✅ S-au extras și mapat {len(all_data)} tweet-uri ROFF direct în categoriile finale.")
    print(f"💾 Salvat în: {output_file}")

if __name__ == "__main__":
    convert_roff()
