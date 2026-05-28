import os
import json
import glob
import re

def load_regexes_and_keywords(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lexicon = json.load(f)
            
        compiled_patterns = {}
        for category, items in lexicon.items():
            if category == "placeholders":
                continue
                
            patterns_for_category = []
            if category == "regex_patterns_comprehensive":
                for pattern in items:
                    try:
                        # Compile explicit standard regexes
                        patterns_for_category.append(re.compile(pattern, re.IGNORECASE))
                    except re.error:
                        print(f"Eroare la compilarea regex-ului: {pattern}")
            else:
                for word in items:
                    # Escape special characters for normal words
                    escaped_word = re.escape(str(word))
                    # Try to use word boundaries to avoid false positives (e.g. matching 'fut' inside 'viitor/futur')
                    prefix = r'\b' if escaped_word[0].isalnum() else ''
                    suffix = r'\b' if escaped_word[-1].isalnum() else ''
                    
                    try:
                        patterns_for_category.append(re.compile(fr"{prefix}{escaped_word}{suffix}", re.IGNORECASE))
                    except re.error:
                        pass
            
            compiled_patterns[category] = patterns_for_category
            
        return compiled_patterns
    except Exception as e:
        print(f"Eroare la încărcarea {filepath}: {e}")
        return {}

def check_toxicity_regex(text, compiled_patterns):
    """
    Checks the text against all compiled patterns.
    Returns (is_toxic, category, matched_word)
    """
    for category, patterns in compiled_patterns.items():
        for pattern in patterns:
            match = pattern.search(text)
            if match:
                return True, category, match.group(0)
                
    return False, None, None

def verify_files():
    # Setup paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    regexes_path = os.path.join(project_dir, 'regexes.json')
    
    # Load and compile patterns
    print(f"Încărcăm dicționarul din: {regexes_path}")
    compiled_patterns = load_regexes_and_keywords(regexes_path)
    if not compiled_patterns:
        print("Nu am putut încărca dicționarul de cuvinte.")
        return

    # Find target files
    search_pattern = os.path.join(script_dir, "scraped_*_data.json")
    files = glob.glob(search_pattern)
    
    if not files:
        print(f"Nu am găsit fișiere 'scraped_*_data.json' în directorul {script_dir}")
        return

    print(f"\n--- 🕵️ Validator de Toxicitate (Regex & Keywords) ---")

    total_kept = 0
    total_removed = 0

    for filepath in files:
        print(f"\nProcesez fișierul: {os.path.basename(filepath)}...")
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f"Eroare la citirea {filepath}: {e}")
            continue

        verified_data = []
        
        for item in data:
            text = item.get("text", "")
            
            is_toxic, category, matched_word = check_toxicity_regex(text, compiled_patterns)
            
            if is_toxic:
                item["category"] = category
                item["matched_word"] = matched_word.lower()
                verified_data.append(item)
            else:
                total_removed += 1
                
        # Save the verified comments to a new file prefixed with 'categorized_'
        filename = os.path.basename(filepath)
        output_filename = filename.replace("scraped_", "categorized_")
        output_file = os.path.join(script_dir, output_filename)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(verified_data, f, ensure_ascii=False, indent=2)
            
        kept = len(verified_data)
        total_kept += kept
        print(f"  ✅ Toxice păstrate: {kept} | Inofensive eliminate: {len(data) - kept}")
        print(f"  💾 Salvat în: {output_filename}")

    print("\n--- 🏁 Raport Final ---")
    print(f"Total comentarii confirmate (conțin cuvinte din dicționar): {total_kept}")
    print(f"Total comentarii eliminate (nu conțin cuvinte): {total_removed}")

if __name__ == "__main__":
    verify_files()
