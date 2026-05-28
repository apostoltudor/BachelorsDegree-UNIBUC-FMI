import numpy as np
import matplotlib.pyplot as plt

def simuleaza_traiectorie(n, p):
    pasi = np.random.choice([-1, 1], size=n, p=[1-p, p])
    traiectorie = np.cumsum(np.insert(pasi, 0, 0))  
    return traiectorie

def simuleaza_pozitii_finale(n, p, numar_simulari):
    pozitii_finale = []
    for _ in range(numar_simulari):
        pasi = np.random.choice([-1, 1], size=n, p=[1-p, p])
        pozitie_finala = np.sum(pasi)
        pozitii_finale.append(pozitie_finala)
    return pozitii_finale

def main():
    p = float(input("probabilitatea p pentru +1: "))
    n = int(input("numarul de pasi n: "))
    numar_simulari = int(input("numarul de simulari: "))

    traiectorie = simuleaza_traiectorie(n, p)
    plt.figure(figsize=(12, 6))
    plt.plot(traiectorie, label='traiectorie')
    plt.title('traiectoria mersului aleator')
    plt.xlabel('pasi')
    plt.ylabel('pozitie')
    plt.grid(True)
    plt.legend()
    plt.show()

    pozitii_finale = simuleaza_pozitii_finale(n, p, numar_simulari)

    plt.figure(figsize=(12, 6))
    plt.hist(pozitii_finale, bins=50, alpha=0.5, color='blue', edgecolor='black', density=True, label='histograma pozitii finale')

    mu = 2 * p - 1
    sigma2 = 4 * p * (1 - p)
    x = np.linspace(min(pozitii_finale), max(pozitii_finale), 1000)
    density = (1 / np.sqrt(2 * np.pi * n * sigma2)) * np.exp(-(x - n * mu)**2 / (2 * n * sigma2))
    plt.plot(x, density, 'r-', lw=2, label='densitate teoretica')

    plt.title('histograma si densitatea teoretica pentru pozitii finale')
    plt.xlabel('pozitie finala')
    plt.ylabel('densitate')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()