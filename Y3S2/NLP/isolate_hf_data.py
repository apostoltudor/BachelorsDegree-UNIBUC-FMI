import json
import os

def isolate_hf():
    v3_file = 'dataset_v3_deduplicated.json'
    v4_file = 'dataset_v4_final.json'
    output_file = 'dataset_hf_contributions.json'

    if not os.path.exists(v3_file) or not os.path.exists(v4_file):
        print("Error: Missing dataset files (v3 or v4).")
        return

    with open(v3_file, 'r', encoding='utf-8') as f:
        v3_data = json.load(f)
    
    with open(v4_file, 'r', encoding='utf-8') as f:
        v4_data = json.load(f)

    # Convert v3 to a set of texts for fast lookup
    v3_texts = {item['text'] for item in v3_data}
    
    # Isolate items in v4 that are NOT in v3
    hf_only = [item for item in v4_data if item['text'] not in v3_texts]

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(hf_only, f, ensure_ascii=False, indent=2)

    print(f"--- Isolation Complete ---")
    print(f"v3 Size: {len(v3_data)}")
    print(f"v4 Size: {len(v4_data)}")
    print(f"Extracted Hugging Face items: {len(hf_only)}")
    print(f"Saved to: {output_file}")

if __name__ == "__main__":
    isolate_hf()
