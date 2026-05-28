import numpy as np
import matplotlib.pyplot as plt

def simuleaza_traiectorie(n):
    pasi = np.random.choice([-1/np.sqrt(0.5), 0, 1/np.sqrt(0.5)], size=n, p=[0.25, 0.5, 0.25])
    traiectorie = np.cumsum(np.insert(pasi, 0, 0)) 
    return traiectorie

def simuleaza_pozitii_finale(n, numar_simulari):
    pozitii_finale = []
    for _ in range(numar_simulari):
        pasi = np.random.choice([-1/np.sqrt(0.5), 0, 1/np.sqrt(0.5)], size=n, p=[0.25, 0.5, 0.25])
        pozitie_finala = np.sum(pasi)
        pozitii_finale.append(pozitie_finala)
    return pozitii_finale

def plot_histogram_and_density(pozitii_finale, n, miu, sigma2):
    plt.figure(figsize=(12, 6))
    plt.hist(pozitii_finale, bins=50, alpha=0.5, color='blue', edgecolor='black', density=True, label='histograma pozitii finale')

    x = np.linspace(min(pozitii_finale), max(pozitii_finale), 1000)
    density = (1 / np.sqrt(2 * np.pi * n * sigma2)) * np.exp(-((x - n * miu)**2) / (2 * n * sigma2))
    plt.plot(x, density, 'r-', lw=2, label='densitate teoretica')

    plt.title('histograma si functia de densitate pentru pozitiile finale')
    plt.xlabel('pozitie finala')
    plt.ylabel('densitate')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    n = int(input("numarul de pasi n: "))
    numar_simulari = int(input("numarul de simulari: "))

    traiectorie = simuleaza_traiectorie(n)
    plt.figure(figsize=(12, 6))
    plt.plot(traiectorie, label='traiectorie')
    plt.title('traiectoria mersului aleator')
    plt.xlabel('pasi')
    plt.ylabel('pozitie')
    plt.grid(True)
    plt.legend()
    plt.show()

    pozitii_finale = simuleaza_pozitii_finale(n, numar_simulari)

    miu = 0.25 * (-1/np.sqrt(0.5)) + 0.5 * 0 + 0.25 * (1/np.sqrt(0.5))
    sigma2 = 0.25 * ((-1/np.sqrt(0.5)) - miu)**2 + 0.5 * (0 - miu)**2 + 0.25 * ((1/np.sqrt(0.5)) - miu)**2

    plot_histogram_and_density(pozitii_finale, n, miu, sigma2)

if __name__ == "__main__":
    main()