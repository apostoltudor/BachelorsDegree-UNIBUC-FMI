import os
import json
import re
from collections import Counter
import matplotlib.pyplot as plt

# ==========================================
# CONFIGURAȚIE
# ==========================================
JSON_FILES = [
    "reddit_aggregated_categorized.json",
    "categorized_news_ro_data.json",
    "categorized_ro_fb_data.json",
    # "categorized_reddit_data.json",
    "categorized_roff_data.json",
    "dataset_v8_balanced.json",
]

# Cuvintele specifice pe care vrem să le căutăm
TARGET_WORDS = ["du-te", "pula", "dracu", "pizda", "muie", "prost"]

# Stopwords de bază în română pentru a nu ne umple top 10 cu "și", "de", "la" etc.
STOP_WORDS = {
    "si", "de", "la", "in", "pe", "un", "o", "cu", "sa", "ca", "nu", "este", "e", 
    "care", "mai", "din", "pentru", "ce", "au", "sunt", "fost", "sau", "se", "dar", 
    "cum", "daca", "iar", "prin", "acest", "aceasta", "tot", "al", "ai", "ale", 
    "lor", "lui", "cel", "cea", "cei", "cele", "unui", "unei", "unor", "niște", 
    "niste", "am", "are", "ati", "a", "te", "ma", "va", "imi", "iti", "isi", "ne",
    "bine", "da", "ba", "cand", "nici", "deci", "doar", "fara", "pana", "asa"
}

def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Eroare la citirea {filepath}: {e}")
        return []

def remove_diacritics(text):
    diacritics = {'ă': 'a', 'â': 'a', 'î': 'i', 'ș': 's', 'ț': 't', 'ş': 's', 'ţ': 't'}
    for char, replacement in diacritics.items():
        text = text.replace(char, replacement)
    return text

def tokenize(text):
    """
    Extrage cuvintele dintr-un text, convertindu-le la litere mici, eliminând diacriticele și semnele de punctuație.
    Păstrează cuvintele cu cratimă (ex: "du-te", "ma-tii").
    """
    text = remove_diacritics(text.lower())
    # Folosim regex pentru a găsi cuvinte care pot conține litere, cifre și cratimă
    words = re.findall(r'\b[\w-]+\b', text)
    return words

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    for filename in JSON_FILES:
        filepath = os.path.join(script_dir, filename)
        if not os.path.exists(filepath):
            print(f"Avertisment: Fișierul '{filename}' nu a fost găsit. Se omite.")
            continue
            
        print(f"\n{'='*60}")
        print(f"🔍 ANALIZĂ PROFUNDĂ PENTRU: {filename}")
        print(f"{'='*60}")
        
        data = load_data(filepath)
        if not data:
            continue
            
        word_counts_per_comment = []
        all_words_counter = Counter()
        target_words_counter = Counter({word: 0 for word in TARGET_WORDS})
        
        for item in data:
            text = item.get("text", "")
            tokens = tokenize(text)
            
            # 1. Numărul de cuvinte per comentariu
            word_counts_per_comment.append(len(tokens))
            
            # 2 & 3. Frecvența cuvintelor (ignorăm stopwords pentru Top 10)
            for token in tokens:
                if token not in STOP_WORDS and len(token) > 1: # Ignorăm cuvintele de o literă
                    all_words_counter[token] += 1
                    
                # Verificăm cuvintele țintă (căutare exactă sau parțială în cazul unor variații)
                for target in TARGET_WORDS:
                    if target == token:
                        target_words_counter[target] += 1

        # --- Afișare Rezultate ---
        
        # Statistici generale
        total_comments = len(word_counts_per_comment)
        avg_words = sum(word_counts_per_comment) / total_comments if total_comments > 0 else 0
        
        print(f"\n📝 Statistici Generale:")
        print(f"  - Total comentarii: {total_comments}")
        print(f"  - Media de cuvinte / comentariu: {avg_words:.2f}")
        print(f"  - Cel mai lung comentariu: {max(word_counts_per_comment)} cuvinte")
        print(f"  - Cel mai scurt comentariu: {min(word_counts_per_comment)} cuvinte")

        # Top 10 cele mai folosite cuvinte
        print(f"\n🏆 Top 10 cele mai folosite cuvinte (fără cuvinte de legătură):")
        top_10 = all_words_counter.most_common(10)
        for i, (word, count) in enumerate(top_10, 1):
            print(f"  {i}. '{word}' (apariții: {count})")
            
        # Frecvența cuvintelor țintă
        print(f"\n🎯 Frecvența cuvintelor țintă alese de tine:")
        # Sortăm după numărul de apariții
        sorted_targets = sorted(target_words_counter.items(), key=lambda x: x[1], reverse=True)
        for word, count in sorted_targets:
            print(f"  - '{word}': {count} apariții")

        # --- Generare Histogramă pentru numărul de cuvinte per comentariu ---
        plt.figure(figsize=(12, 6))
        
        # Setăm bins (intervale) logice. Majoritatea comentariilor sunt sub 100 de cuvinte.
        bins = range(0, min(max(word_counts_per_comment), 150) + 5, 5)
        
        plt.hist(word_counts_per_comment, bins=bins, color='mediumpurple', edgecolor='black', alpha=0.7)
        plt.title(f'Histogramă: Distribuția lungimii comentariilor (în cuvinte)\n[{filename}]', fontsize=14)
        plt.xlabel('Număr de cuvinte per comentariu', fontsize=12)
        plt.ylabel('Frecvență (Număr de comentarii)', fontsize=12)
        
        # Adăugăm o linie verticală pentru medie
        plt.axvline(avg_words, color='red', linestyle='--', linewidth=2, label=f'Medie ({avg_words:.1f})')
        plt.legend()
        
        plt.tight_layout()
        output_img = os.path.join(script_dir, f"deep_analysis_words_{filename.replace('.json', '.png')}")
        plt.savefig(output_img, dpi=300)
        print(f"\n📊 Histograma lungimii comentariilor salvată ca: {os.path.basename(output_img)}")
        plt.close()

if __name__ == "__main__":
    main()
