import os
import csv
import json
import glob

def csv_to_json_mapped():
    # Setup paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    csv_dir = os.path.join(project_dir, 'categorii_split')
    
    # Find all CSV files
    search_pattern = os.path.join(csv_dir, "*.csv")
    csv_files = glob.glob(search_pattern)
    
    if not csv_files:
        print(f"Nu am găsit fișiere CSV în {csv_dir}")
        return

    all_data = []
    
    # Mapping the labels from the CSVs (ABUSE, INSULT, PROFANITY, OTHER) 
    # to the predefined categories. Since they are all broadly toxic,
    # "General Aggression & Insults" is the most accurate fit.
    label_mapping = {
        "ABUSE": "General Aggression & Insults",
        "INSULT": "General Aggression & Insults",
        "PROFANITY": "Family & Religious Invective",
        "OTHER": "Neutral"
    }
    
    print(f"--- 🔄 Mapare Directă CSV-uri (categorii_split) în JSON ---")
    for filepath in csv_files:
        filename = os.path.basename(filepath)
        print(f"Procesez: {filename}...")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    text = row.get('text', '').strip()
                    label = row.get('label', '').strip()
                    
                    category = label_mapping.get(label, "General Aggression & Insults")
                    
                    if text:
                        all_data.append({
                            "text": text,
                            "category": category,
                            "source": f"csv/categorii_split/{label}"
                        })
        except Exception as e:
            print(f"Eroare la citirea {filename}: {e}")

    # Output directly to categorized_ to bypass check_offensive.py
    output_file = os.path.join(script_dir, "categorized_csv_data.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
        
    print(f"\n✅ S-au extras și mapat {len(all_data)} comentarii din CSV-uri direct în categoriile finale.")
    print(f"💾 Salvat în: {output_file}")

if __name__ == "__main__":
    csv_to_json_mapped()
