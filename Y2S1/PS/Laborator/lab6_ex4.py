import numpy as np
import matplotlib.pyplot as plt

def genereaza_geometric_a(p, numar_simulari):
    u = np.random.uniform(0, 1, numar_simulari)
    x = np.ceil(np.log(u) / np.log(1 - p)).astype(int)
    return x

def genereaza_geometric_b(p, numar_simulari):
    x = np.random.geometric(p, numar_simulari)
    return x

def afiseaza_histograma(rezultate, titlu):
    plt.hist(rezultate, bins=range(1, max(rezultate) + 1), alpha=0.7, color='skyblue', edgecolor='black', density=True)
    plt.title(titlu)
    plt.xlabel('valoare')
    plt.ylabel('frecvența')
    plt.grid(True)
    plt.show()

def afiseaza_grafic_ponderi(p, n):
    k_values = np.arange(1, n + 1)
    ponderi = (1 - p) ** (k_values - 1) * p
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
    p = float(input("probabilitatea p: "))
    numar_simulari = int(input("simulari: "))
    n = int(input("n pt graficul ponderilor: "))

    rezultate_a = genereaza_geometric_a(p, numar_simulari)
    rezultate_b = genereaza_geometric_b(p, numar_simulari)

    afiseaza_histograma(rezultate_a, 'histograma - metoda A')
    afiseaza_histograma(rezultate_b, 'histograma - metoda B')

    afiseaza_grafic_ponderi(p, n)

    media_a, varianta_a = estimeaza_media_si_varianta(rezultate_a)
    media_b, varianta_b = estimeaza_media_si_varianta(rezultate_b)

    print(f"metoda A - media: {media_a:.4f}, varianta: {varianta_a:.4f}")
    print(f"metoda B - media: {media_b:.4f}, varianta: {varianta_b:.4f}")

if __name__ == "__main__":
    main()