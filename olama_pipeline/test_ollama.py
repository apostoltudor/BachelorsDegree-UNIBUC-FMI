import requests
import json
import sys

def test_ollama():
    base_url = "http://localhost:11434"
    
    print(f"--- Testing Ollama on {base_url} ---")
    
    # 1. Test GET /api/tags (Check if service is alive and list models)
    print("\n[1/2] Testing GET /api/tags (Check service & models)...")
    try:
        response = requests.get(f"{base_url}/api/tags")
        if response.status_code == 200:
            print("✅ Success! Ollama is reachable.")
            models = response.json().get('models', [])
            print(f"Available models: {[m['name'] for m in models]}")
        else:
            print(f"❌ Failed. Status code: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"❌ Connection Error: {e}")

    # 2. Test POST /api/generate (Check generation capability)
    print("\n[2/2] Testing POST /api/generate (Check Llama3 generation)...")
    payload = {
        "model": "llama3",
        "prompt": "Salut! Zi-mi o glumă scurtă.",
        "stream": False
    }
    try:
        # Note: Using POST is mandatory for /api/generate
        response = requests.post(f"{base_url}/api/generate", json=payload)
        if response.status_code == 200:
            result = response.json()
            print("✅ Success! Generation works.")
            print(f"Response from Llama3: {result.get('response')}")
        elif response.status_code == 405:
            print("❌ Error 405: Method Not Allowed.")
            print("   This usually happens if you try to GET /api/generate instead of POST.")
        else:
            print(f"❌ Failed. Status code: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"❌ Connection Error: {e}")

if __name__ == "__main__":
    test_ollama()
