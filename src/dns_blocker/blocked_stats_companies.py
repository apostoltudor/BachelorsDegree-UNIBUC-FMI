import matplotlib.pyplot as plt
from collections import Counter

LOG_FILE = "blocked_requests.log"
OUTPUT_IMAGE = "blocked_stats_companies.png"

# Citește log-ul
with open(LOG_FILE, "r") as f:
    domains = [line.strip().lower() for line in f.readlines()]

# Dicționarul cu companii și cuvintele cheie
COMPANIES = {
    "Google": ["google", "youtube", "doubleclick", "gstatic", "googlesyndication"],
    "Facebook": ["facebook", "fbcdn", "fb", "instagram"],
    "Amazon": ["amazon", "cloudfront", "amazonaws"],
    "Microsoft": ["microsoft", "windows", "live", "office"],
    "Twitter": ["twitter", "twimg"],
    "Apple": ["apple", "icloud", "mzstatic"],
}

def find_company(domain):
    for company, keywords in COMPANIES.items():
        for kw in keywords:
            if kw in domain:
                return company
    return "Other"

# Map domains to companies
company_list = [find_company(d) for d in domains]

# Contorizează blocările pe companii
counts = Counter(company_list)
most_common = counts.most_common()

# Print raport
print("Raport blocări pe companii:")
for company, count in most_common:
    print(f"{company}: {count}")

# Grafic
labels, values = zip(*most_common)
plt.figure(figsize=(10,6))
plt.bar(labels, values, color='skyblue')
plt.xlabel("Companii")
plt.ylabel("Număr de blocări")
plt.title("Blocări DNS pe companii (top)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(OUTPUT_IMAGE)
print(f"Grafic salvat ca {OUTPUT_IMAGE}")
