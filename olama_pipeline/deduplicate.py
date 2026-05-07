import json
import os
import re

def normalize_text(text):
    # Lowercase, remove punctuation, and collapse whitespace for "near-duplicate" detection
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = " ".join(text.split())
    return text

def deduplicate():
    input_file = 'dataset_v2_augmented.json'
    output_file = 'dataset_v3_deduplicated.json'
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    initial_count = len(data)
    seen_normalized = set()
    unique_data = []
    duplicates_count = 0

    for entry in data:
        norm = normalize_text(entry['text'])
        if norm not in seen_normalized:
            seen_normalized.add(norm)
            unique_data.append(entry)
        else:
            duplicates_count += 1

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(unique_data, f, ensure_ascii=False, indent=2)

    print(f"--- Deduplication Complete ---")
    print(f"Initial entries: {initial_count}")
    print(f"Duplicates removed: {duplicates_count}")
    print(f"Final unique entries: {len(unique_data)}")
    
    # Show balance after deduplication
    counts = {}
    for d in unique_data:
        counts[d['category']] = counts.get(d['category'], 0) + 1
    
    print("\nFinal Category Distribution:")
    for cat, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
        print(f" - {cat}: {count}")

if __name__ == "__main__":
    deduplicate()
