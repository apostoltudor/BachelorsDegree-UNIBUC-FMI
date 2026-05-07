import os
import requests
import json
from dotenv import load_dotenv

# Load the token
load_dotenv(dotenv_path="hf_pipeline/.env")
token = os.getenv("HF_TOKEN").strip() if os.getenv("HF_TOKEN") else None

# Romanian model
model_id = "OpenLLM-Ro/RoLlama3.1-8B-Instruct"
# Fallback model (if the router doesn't support the Romanian one yet)
fallback_model = "meta-llama/Llama-3.1-8B-Instruct"

# Modern Router API
API_URL = "https://router.huggingface.co/v1/chat/completions"

def query(prompt, model):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "Ești un expert în argou românesc."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 150
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def test_connectivity():
    print(f"--- Final Connectivity Test ---")
    print(f"Token: hf_...{token[-4:] if token else 'None'}")
    
    # Try Romanian model first
    print(f"\nAttempting Romanian Model: {model_id}...")
    res = query("Salut! Spune-mi o înjurătură românească ușoară.", model_id)
    
    if "choices" in res:
        print("✅ Romanian Model Success!")
        print(res['choices'][0]['message']['content'])
    else:
        print(f"❌ Romanian Model Failed: {res.get('error', res)}")
        
        # Try Fallback
        print(f"\nAttempting Fallback Model: {fallback_model}...")
        res = query("Salut!", fallback_model)
        if "choices" in res:
            print("✅ Fallback Model Success!")
        else:
            print(f"❌ Fallback Model Failed: {res.get('error', res)}")

if __name__ == "__main__":
    test_connectivity()
