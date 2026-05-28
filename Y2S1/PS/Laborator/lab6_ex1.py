import numpy as np
import matplotlib.pyplot as plt
import math

def binomial_a(n, p, numar_simulari):
    rezultate = []
    for _ in range(numar_simulari):
        probabilitati = [math.comb(n, k) * (p**k) * ((1-p)**(n-k)) for k in range(n + 1)]
        k = np.random.choice(range(n + 1), p=probabilitati)
        rezultate.append(k)
    return rezultate

def binomial_b(n, p, numar_simulari):
    rezultate = []
    for _ in range(numar_simulari):
        x = np.random.binomial(1, p, n)
        rezultate.append(np.sum(x))
    return rezultate

def binomial_c(n, p, numar_simulari):
    return np.random.binomial(n, p, numar_simulari)

def afiseaza_histograma(rezultate, titlu):
    plt.hist(rezultate, bins=range(min(rezultate), max(rezultate) + 1), alpha=0.7, color='skyblue', edgecolor='black')
    plt.title(titlu)
    plt.xlabel('valoare')
    plt.ylabel('frecvența')
    plt.grid(True)
    plt.show()

def afiseaza_grafic_ponderi(n, p):
    k_values = range(n + 1)
    ponderi = [math.comb(n, k) * (p**k) * ((1-p)**(n-k)) for k in k_values]
    plt.plot(k_values, ponderi, marker='o', linestyle='-', color='red')
    plt.title('graficul ponderilor')
    plt.xlabel('k')
    plt.ylabel('ponderi')
    plt.grid(True)
    plt.show()

def estimeaza_media_si_varianta(rezultate):
    media = np.mean(rezultate)
    varianta = np.var(rezultate)
    return media, varianta

def main():
    n = int(input("n: "))
    p = float(input("p: "))
    numar_simulari = int(input("nr de simulari: "))

    rezultate_a = binomial_a(n, p, numar_simulari)
    rezultate_b = binomial_b(n, p, numar_simulari)
    rezultate_c = binomial_c(n, p, numar_simulari)

    afiseaza_histograma(rezultate_a, 'histogramă - metoda A')
    afiseaza_histograma(rezultate_b, 'histogramă - metoda B')
    afiseaza_histograma(rezultate_c, 'histogramă - metoda C')

    afiseaza_grafic_ponderi(n, p)

    media_a, varianta_a = estimeaza_media_si_varianta(rezultate_a)
    media_b, varianta_b = estimeaza_media_si_varianta(rezultate_b)
    media_c, varianta_c = estimeaza_media_si_varianta(rezultate_c)

    print(f"metoda A - media: {media_a:.4f}, varianta: {varianta_a:.4f}")
    print(f"metoda B - media: {media_b:.4f}, varianta: {varianta_b:.4f}")
    print(f"metoda C - media: {media_c:.4f}, varianta: {varianta_c:.4f}")

if __name__ == "__main__":
    main()