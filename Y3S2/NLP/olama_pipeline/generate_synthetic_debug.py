import requests
import json
import time
import sys

# Ensure output handles Romanian characters correctly in terminal
sys.stdout.reconfigure(encoding='utf-8')

def generate_sentence(category, examples):
    url = "http://localhost:11434/api/generate"
    
    # We ask for one sentence at a time for maximum control and visibility
    prompt = f"""
Ești un expert în lingvistică și analiză de text toxic în limba română. 
Sarcina ta este să generezi o singură frază toxică/insultătoare NOUĂ care să se potrivească perfect categoriei: "{category}".

Iată câteva exemple de referință pentru ton și stil:
{chr(10).join(['- ' + ex for ex in examples])}

Cerințe:
1. Generază o SINGURĂ frază.
2. Folosește un limbaj agresiv, specific românesc (argou, înjurături, insulte).
3. Nu repeta exemplele de mai sus.
4. Răspunde DOAR cu fraza generată, fără explicații.

Fraza nouă:"""

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.8,
            "top_p": 0.9
        }
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json().get('response', '').strip().replace('"', '')
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Exception: {e}"

def debug_generation():
    # Define which category to debug
    target_category = "Misogyny & Objectification"
    
    # Load initial examples for few-shot prompting
    try:
        with open('dataset_v1.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: dataset_v1.json not found.")
        return

    # Filter examples for our target category
    examples = [d['text'] for d in data if d['category'] == target_category][:5]
    
    print(f"--- Debugging Generation for Category: {target_category} ---")
    print(f"Using {len(examples)} reference examples.")
    print("Press Ctrl+C to stop.\n")

    generated_count = 0
    results = []

    try:
        for i in range(1, 11): # Let's generate 10 for debugging
            print(f"[{i}/10] Generating...", end="\r")
            sentence = generate_sentence(target_category, examples)
            
            # Print immediately for user visibility
            print(f"[{i}/10] Result: {sentence}")
            
            results.append({"text": sentence, "category": target_category})
            generated_count += 1
            time.sleep(0.5) # Small sleep to not overwhelm the UI
            
    except KeyboardInterrupt:
        print("\nStopped by user.")

    print(f"\n--- Debug Session Finished ---")
    print(f"Generated {generated_count} sentences.")
    
    # Optional: save debug results
    if results:
        with open('debug_synthetic_results.json', 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print("Results saved to debug_synthetic_results.json")

if __name__ == "__main__":
    debug_generation()
