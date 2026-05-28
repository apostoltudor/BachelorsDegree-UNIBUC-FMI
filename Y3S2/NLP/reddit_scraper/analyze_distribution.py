import json
import os

def analyze_reddit_distribution():
    files = {
        "r/romania": "reddit_scraper/classified_romania.json",
        "r/Roumanie": "reddit_scraper/classified_roumanie.json"
    }
    
    overall_counts = {}
    
    print("--- 📊 Reddit Category Distribution ---")
    
    for sub, path in files.items():
        if not os.path.exists(path):
            print(f"File not found: {path}")
            continue
            
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        counts = {}
        for item in data:
            cat = item['category']
            counts[cat] = counts.get(cat, 0) + 1
            overall_counts[cat] = overall_counts.get(cat, 0) + 1
            
        print(f"\n[{sub}] - Total: {len(data)}")
        for cat, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
            print(f"  - {cat}: {count} ({round(count/len(data)*100, 1)}%)")

    print("\n[COMBINED REDDIT DATA]")
    total_combined = sum(overall_counts.values())
    for cat, count in sorted(overall_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  - {cat}: {count} ({round(count/total_combined*100, 1)}%)")

if __name__ == "__main__":
    analyze_reddit_distribution()
