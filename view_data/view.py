import json
import re
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import networkx as nx

# 1. Funcție de curățare a textului
def curata_text(text):
    # Transformăm totul în litere mici
    text = text.lower()
    # Păstrăm și cuvintele cu cratimă (ex: "du-te", "baga-mi-as")
    cuvinte = re.findall(r'\b[a-zăâîșț]+(?:-[a-zăâîșț]+)*\b', text)
    return cuvinte

# 2. Încărcarea datelor
def incarca_date(nume_fisier):
    with open(nume_fisier, 'r', encoding='utf-8') as f:
        date = json.load(f)
    
    # Presupunem că JSON-ul este o listă simplă de stringuri
    # Dacă JSON-ul e o listă de dicționare, de ex: [{"text": "injuratura"}, ...], modifică aici:
    # texte = [item['text'] for item in date]
    texte = date 
    return texte

# ==========================================
# GRAFIC 1: Cele mai utilizate cuvinte
# ==========================================
def grafic_frecventa(toate_cuvintele, top_n=20):
    frecvente = Counter(toate_cuvintele)
    df = pd.DataFrame(frecvente.most_common(top_n), columns=['Cuvânt', 'Frecvență'])
    
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Frecvență', y='Cuvânt', data=df, palette='Reds_r')
    plt.title(f'Top {top_n} cele mai folosite cuvinte', fontsize=16)
    plt.xlabel('Număr de apariții')
    plt.ylabel('Cuvânt')
    plt.tight_layout()
    plt.savefig('top_cuvinte.png')
    plt.show()

# ==========================================
# GRAFIC 2: WordCloud (Nor de cuvinte)
# ==========================================
def grafic_wordcloud(toate_cuvintele):
    text_complet = ' '.join(toate_cuvintele)
    wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='inferno').generate(text_complet)
    
    plt.figure(figsize=(15, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Norul de cuvinte', fontsize=20)
    plt.savefig('wordcloud.png')
    plt.show()

# ==========================================
# GRAFIC 3: Rețeaua de cuvinte (Cum se leagă)
# ==========================================
def grafic_retea_bigrame(lista_texte, top_n_perechi=30):
    toate_bigramele = []
    
    for text in lista_texte:
        cuvinte = curata_text(text)
        # Creăm perechi de cuvinte consecutive (ex: "du-te", "dracu")
        for i in range(len(cuvinte) - 1):
            toate_bigramele.append((cuvinte[i], cuvinte[i+1]))
            
    frecvente_bigrame = Counter(toate_bigramele)
    top_bigrame = frecvente_bigrame.most_common(top_n_perechi)
    
    # Construim graful de rețea
    G = nx.Graph()
    for (cuvant1, cuvant2), frecventa in top_bigrame:
        G.add_edge(cuvant1, cuvant2, weight=frecventa)
        
    plt.figure(figsize=(14, 10))
    pos = nx.spring_layout(G, k=0.5, iterations=50) # Modul în care se împrăștie nodurile
    
    # Grosimea liniilor bazată pe frecvență
    weights = [G[u][v]['weight'] for u,v in G.edges()]
    max_weight = max(weights) if weights else 1
    linewidths = [(w / max_weight) * 5 for w in weights]
    
    nx.draw_networkx_nodes(G, pos, node_color='lightcoral', node_size=3000, alpha=0.8)
    nx.draw_networkx_edges(G, pos, width=linewidths, edge_color='gray', alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    
    plt.title(f'Cum se leagă cuvintele (Top {top_n_perechi} conexiuni)', fontsize=16)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('retea_cuvinte.png')
    plt.show()

# ==========================================
# Execuția principală
# ==========================================
if __name__ == "__main__":
    nume_fisier = "C:\\Users\\Cosmin\\Documents\\NLP\\regexes.json" # <-- PUNE NUMELE FIȘIERULUI TĂU AICI
    
    try:
        texte = incarca_date(nume_fisier)
        toate_cuvintele = []
        for t in texte:
            toate_cuvintele.extend(curata_text(t))
            
        print("Generez graficul de frecvență...")
        grafic_frecventa(toate_cuvintele)
        
        print("Generez norul de cuvinte...")
        grafic_wordcloud(toate_cuvintele)
        
        print("Generez rețeaua de cuvinte...")
        grafic_retea_bigrame(texte)
        
        print("Gata! Graficele au fost salvate și ca imagini (.png) în același folder.")
        
    except FileNotFoundError:
        print(f"Eroare: Nu am putut găsi fișierul '{nume_fisier}'. Asigură-te că e în același folder cu scriptul.")