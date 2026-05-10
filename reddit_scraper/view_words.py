import json
import re
from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt

def curata_text(text):
    if not text or text is None:
        return []
    text = str(text).lower()
    # Păstrăm cratimele, eliminăm restul
    cuvinte = re.findall(r'\b[a-zăâîșț]+(?:-[a-zăâîșț]+)*\b', text)
    return cuvinte

def genereaza_harta_aerisita(nume_fisier, top_n=40):
    try:
        with open(nume_fisier, 'r', encoding='utf-8') as f:
            date = json.load(f)
    except Exception as e:
        print(f"Eroare: {e}")
        return

    stop_words = {
        'si', 'la', 'de', 'ca', 'un', 'o', 'pe', 'cu', 'nu', 'mai', 'sa', 'da', 
        'ce', 'dar', 'va', 'pentru', 'din', 'care', 'sunt', 'este', 'asta',
        'au', 'fost', 'tot', 'prin', 'ale', 'lor', 'sau', 'aceasta', 'faca', 
        'acum', 'null', 'not', 'nan', 'none', 'este', 'era', 'ar', 'unei', 'unui'
    }

    toate_bigramele = []
    for item in date:
        text = item.get('text', '')
        cuvinte = curata_text(text)
        cuvinte_filtrate = [c for c in cuvinte if c not in stop_words and len(c) > 2]
        
        for i in range(len(cuvinte_filtrate) - 1):
            toate_bigramele.append((cuvinte_filtrate[i], cuvinte_filtrate[i+1]))

    frecventa_perechi = Counter(toate_bigramele)
    cele_mai_dese = frecventa_perechi.most_common(top_n)

    G = nx.Graph()
    for (c1, c2), scor in cele_mai_dese:
        G.add_edge(c1, c2, weight=scor)

    # --- SETĂRI PENTRU SPAȚIERE ---
    plt.figure(figsize=(20, 14)) # Mărim considerabil suprafața desenului
    
    # k: distanța între noduri (crește-l dacă sunt prea înghesuite, ex: 1.5, 2.0)
    # iterations: de câte ori rulează simularea de respingere
    pos = nx.spring_layout(G, k=1.8, iterations=100, seed=42) 

    # Calculăm grosimea liniilor
    weights = [G[u][v]['weight'] for u, v in G.edges()]
    max_w = max(weights) if weights else 1
    edge_widths = [(w / max_w) * 12 for w in weights]

    # Desenăm nodurile
    nx.draw_networkx_nodes(G, pos, 
                           node_size=4000, 
                           node_color='#ff7675', 
                           alpha=0.85,
                           edgecolors='white',
                           linewidths=2)

    # Desenăm liniile (muchiile)
    nx.draw_networkx_edges(G, pos, 
                           width=edge_widths, 
                           edge_color='#dfe6e9', 
                           alpha=0.7)

    # Desenăm etichetele (cu un font mai curat)
    nx.draw_networkx_labels(G, pos, 
                            font_size=12, 
                            font_weight='bold', 
                            font_family='sans-serif')

    plt.title(f"Harta Conexiunilor (Layout Aerisit) - Top {top_n} Perechi", fontsize=22, pad=30)
    plt.axis('off')
    
    print("✅ Conexiuni procesate. Generez graficul...")
    plt.tight_layout()
    plt.show()

genereaza_harta_aerisita('C:\\Users\\Cosmin\\Documents\\NLP\\reddit_scraper\\categorized_reddit_data.json')