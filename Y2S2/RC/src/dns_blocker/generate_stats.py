import matplotlib.pyplot as plt
from collections import Counter
import re
import os

LOG_FILE = "blocked_requests.log"
OUTPUT_IMAGE = "blocked_stats.png"

if not os.path.exists(LOG_FILE):
    print(f"Fisierul de log '{LOG_FILE}' nu exista.")
    exit(1)

with open(LOG_FILE, "r") as f:
    lines = f.readlines()

# Regex care extrage domeniul din fiecare linie
pattern = re.compile(r"Blocked:\s+([^\s]+)")

domains = [pattern.search(line).group(1) for line in lines if pattern.search(line)]

if not domains:
    print("[Info] Nu au fost găsite domenii în log.")
    exit(0)

counts = Counter(domains)
most_common = counts.most_common(10)  # Top 10 cele mai blocate domenii

labels, values = zip(*most_common)

plt.figure(figsize=(10, 6))
bars = plt.bar(labels, values, color='mediumseagreen')

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.3, str(int(height)), ha='center', va='bottom', fontsize=10)

plt.xlabel("Domenii", fontsize=12)
plt.ylabel("Numar de blocări", fontsize=12)
plt.title("Top 10 domenii blocate", fontsize=14, weight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

plt.savefig(OUTPUT_IMAGE)
print(f"Graficul a fost salvat ca '{OUTPUT_IMAGE}'")
