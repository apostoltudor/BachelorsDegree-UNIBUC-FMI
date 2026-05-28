import numpy as np
import matplotlib.pyplot as plt

def genereaza_exponential(lam, numar_simulari):
    return np.random.exponential(1/lam, numar_simulari)

def main():
    lam1 = float(input("valoarea lui lambda1: "))
    lam2 = float(input("valoarea lui lambda2: "))
    numar_simulari = int(input("numarul de simulari: "))

    x = genereaza_exponential(lam1, numar_simulari)
    y = genereaza_exponential(lam2, numar_simulari)

    z = np.minimum(x, y)

    plt.figure(figsize=(12, 6))
    plt.hist(z, bins=50, alpha=0.5, color='blue', edgecolor='black', density=True, label='Histogramă Z')

    x_values = np.linspace(0, max(z), 1000)
    density = (lam1 + lam2) * np.exp(-(lam1 + lam2) * x_values)
    plt.plot(x_values, density, 'r-', lw=2, label='densitate teoretica')

    plt.title('histograma si functia de densitate pentru Z = min(X, Y)')
    plt.xlabel('valoare')
    plt.ylabel('densitate')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()