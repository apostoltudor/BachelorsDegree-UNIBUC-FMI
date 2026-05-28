import os
import csv
import json

def convert_news_ro():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    csv_path = os.path.join(project_dir, 'news-ro-offense-main', 'news-ro-offense-main', 'comments.csv')
    
    if not os.path.exists(csv_path):
        print(f"File not found: {csv_path}")
        return

    all_data = []
    
    # Mapping based on the requested categories
    label_mapping = {
        "0": "Neutral",                           # Non-offensive
        "1": "General Aggression & Insults",      # Targeted insult
        "2": "Hate Speech & Discriminatory",      # Racist
        "3": "Hate Speech & Discriminatory",      # Homophobic
        "4": "Misogyny & Objectification"         # Sexist
    }
    
    print(f"--- 🔄 Mapare Directă News-RO-Offense CSV în JSON ---")
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                text = row.get('comment_text', '').strip()
                label_num = row.get('LABEL', '').strip()
                
                category = label_mapping.get(label_num, "Neutral")
                
                if text:
                    all_data.append({
                        "text": text,
                        "category": category,
                        "source": "csv/news_ro_offense"
                    })
    except Exception as e:
        print(f"Eroare la citirea {csv_path}: {e}")

    # Output directly to categorized_ to bypass check_offensive.py
    output_file = os.path.join(script_dir, "categorized_news_ro_data.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
        
    print(f"\n✅ S-au extras și mapat {len(all_data)} comentarii direct în categoriile finale.")
    print(f"💾 Salvat în: {output_file}")

if __name__ == "__main__":
    convert_news_ro()
