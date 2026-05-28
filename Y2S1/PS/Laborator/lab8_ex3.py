import numpy as np
import matplotlib.pyplot as plt

def genereaza_simulari_z(n, miu, sigma, numar_simulari):
    z_values = []
    for _ in range(numar_simulari):
        x_values = np.random.normal(miu, sigma, n)
        z = np.sqrt(n) * (np.mean(x_values) - miu) / sigma
        z_values.append(z)
    return z_values

def main():
    miu = float(input("media miu: "))
    sigma = float(input("deviatia standard sigma: "))
    n = int(input("numarul de variabile aleatoare n: "))
    numar_simulari = int(input("numarul de simulari: "))

    z_values = genereaza_simulari_z(n, miu, sigma, numar_simulari)

    plt.figure(figsize=(12, 6))
    plt.hist(z_values, bins=50, alpha=0.5, color='blue', edgecolor='black', density=True, label='Histogramă Z')

    x = np.linspace(min(z_values), max(z_values), 1000)
    density = (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-x**2 / (2 * sigma**2))
    plt.plot(x, density, 'r-', lw=2, label='densitate teoretica')

    plt.title('histograma')
    plt.xlabel('valoare')
    plt.ylabel('densitate')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()