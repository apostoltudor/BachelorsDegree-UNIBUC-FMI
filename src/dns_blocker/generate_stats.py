import matplotlib.pyplot as plt
from collections import Counter

LOG_FILE = "blocked_requests.log"
OUTPUT_IMAGE = "blocked_stats.png"

# Citește log-ul și contorizează domeniile
with open(LOG_FILE, "r") as f:
    domains = [line.strip() for line in f.readlines()]

counts = Counter(domains)
most_common = counts.most_common(10)  # Top 10 domenii blocate

# Separă datele
labels, values = zip(*most_common)

# Creează graficul
plt.figure(figsize=(10, 6))
plt.bar(labels, values, color='crimson')
plt.xlabel("Domenii")
plt.ylabel("Număr de blocări")
plt.title("Top 10 domenii blocate")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Salvează imaginea
plt.savefig(OUTPUT_IMAGE)
print(f"Graficul a fost salvat ca {OUTPUT_IMAGE}")
