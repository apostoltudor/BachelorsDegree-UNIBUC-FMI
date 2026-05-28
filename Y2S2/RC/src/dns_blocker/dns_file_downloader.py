import subprocess
import base64

DNS_SERVER = "127.0.0.1"
PORT = 53535
FILENAME = "secret.txt"

def query_chunk(index):
    domain = f"{FILENAME}.{index}.tunel.live"
    cmd = ["dig", f"@{DNS_SERVER}", "-p", str(PORT), domain, "TXT", "+short"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip().strip('"')

def download_file():
    chunks = []
    index = 0
    while True:
        txt = query_chunk(index)
        print(f"Chunk {index} RAW TXT: '{txt}'")

        if not txt:
            print(f"No data received for chunk {index}, stopping.")
            break
        if txt == "[END]":
            print("Received end of file marker.")
            break
        try:
            decoded = base64.b64decode(txt)
        except Exception as e:
            print(f"Failed to decode base64 chunk {index}: {e}")
            break
        chunks.append(decoded)
        print(f"Downloaded chunk {index}, {len(decoded)} bytes")
        index += 1
    return b"".join(chunks)

if __name__ == "__main__":
    data = download_file()
    if data:
        with open(f"downloaded_{FILENAME}", "wb") as f:
            f.write(data)
        print(f"File saved as downloaded_{FILENAME}")
    else:
        print("No data downloaded.")
