import numpy as np
import matplotlib.pyplot as plt
import math

def genereaza_poisson_a(lam, n, numar_simulari):
    p = lam / n
    rezultate = np.random.binomial(n, p, numar_simulari)
    return rezultate

def genereaza_poisson_b(lam, numar_simulari):
    rezultate = np.random.poisson(lam, numar_simulari)
    return rezultate

def afiseaza_histograma(rezultate, titlu):
    plt.hist(rezultate, bins=range(min(rezultate), max(rezultate) + 1), alpha=0.7, color='skyblue', edgecolor='black', density=True)
    plt.title(titlu)
    plt.xlabel('valoare')
    plt.ylabel('frecventa')
    plt.grid(True)
    plt.show()

def afiseaza_grafic_ponderi(lam, max_k):
    k_values = np.arange(0, max_k + 1)
    ponderi = [math.exp(-lam) * (lam**k) / math.factorial(k) for k in k_values]
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
    lam = float(input("valoarea lui lambda: "))
    n = int(input("valoarea lui n: "))
    numar_simulari = int(input("numarul de simulari: "))

    rezultate_a = genereaza_poisson_a(lam, n, numar_simulari)
    rezultate_b = genereaza_poisson_b(lam, numar_simulari)

    afiseaza_histograma(rezultate_a, 'histograma - metoda A (aproximare binomiala)')
    afiseaza_histograma(rezultate_b, 'histograma - metoda B (generator Poisson)')

    max_k = int(lam * 3)
    afiseaza_grafic_ponderi(lam, max_k)

    media_a, varianta_a = estimeaza_media_si_varianta(rezultate_a)
    media_b, varianta_b = estimeaza_media_si_varianta(rezultate_b)

    print(f"metoda A - media: {media_a:.4f}, varianta: {varianta_a:.4f}")
    print(f"metoda B - media: {media_b:.4f}, varianta: {varianta_b:.4f}")

if __name__ == "__main__":
    main()