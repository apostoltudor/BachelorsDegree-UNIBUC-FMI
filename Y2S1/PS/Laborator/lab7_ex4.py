import numpy as np
import matplotlib.pyplot as plt


def genereaza_exponential_a(lam, numar_simulari):
    u = np.random.uniform(0, 1, numar_simulari)
    x = -1 / lam * np.log(u)
    return x


def genereaza_exponential_b(lam, numar_simulari):
    x = np.random.exponential(1 / lam, numar_simulari)
    return x


def afiseaza_histograme_si_densitate(rezultate_a, rezultate_b, lam):
    plt.figure(figsize=(12, 6))

    plt.hist(rezultate_a, bins=50, alpha=0.5, color='blue', edgecolor='black', density=True, label='Metoda A')

    plt.hist(rezultate_b, bins=50, alpha=0.5, color='green', edgecolor='black', density=True, label='Metoda B')

    x = np.linspace(0, max(max(rezultate_a), max(rezultate_b)), 1000)
    y = lam * np.exp(-lam * x)
    plt.plot(x, y, 'r-', lw=2, label='densitate teoretica')

    plt.title('histograme si functia de densitate')
    plt.xlabel('valoare')
    plt.ylabel('densitate')
    plt.legend()
    plt.grid(True)
    plt.show()


def estimeaza_media_si_varianta(rezultate):
    media = np.mean(rezultate)
    varianta = np.var(rezultate)
    return media, varianta


def afiseaza_distributie_cumulativa(rezultate_a, rezultate_b, lam):
    plt.figure(figsize=(12, 6))

    sorted_a = np.sort(rezultate_a)
    cdf_a = np.arange(1, len(sorted_a) + 1) / len(sorted_a)
    plt.step(sorted_a, cdf_a, where='post', label='CDF metoda A', color='blue')

    sorted_b = np.sort(rezultate_b)
    cdf_b = np.arange(1, len(sorted_b) + 1) / len(sorted_b)
    plt.step(sorted_b, cdf_b, where='post', label='CDF metoda B', color='green')

    x = np.linspace(0, max(max(rezultate_a), max(rezultate_b)), 1000)
    cdf_theoretical = 1 - np.exp(-lam * x)
    plt.plot(x, cdf_theoretical, 'r-', lw=2, label='CDF teoretica')

    plt.title('functia de distributie cumulativa')
    plt.xlabel('valoare')
    plt.ylabel('probabilitate')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    lam = float(input("valoarea lui lambda: "))
    numar_simulari = int(input("numarul de simulari: "))

    rezultate_a = genereaza_exponential_a(lam, numar_simulari)
    rezultate_b = genereaza_exponential_b(lam, numar_simulari)

    afiseaza_histograme_si_densitate(rezultate_a, rezultate_b, lam)

    media_a, varianta_a = estimeaza_media_si_varianta(rezultate_a)
    media_b, varianta_b = estimeaza_media_si_varianta(rezultate_b)

    print(f"metoda A - media: {media_a:.4f}, varianta: {varianta_a:.4f}")
    print(f"metoda B - media: {media_b:.4f}, varianta: {varianta_b:.4f}")

    afiseaza_distributie_cumulativa(rezultate_a, rezultate_b, lam)

if __name__ == "__main__":
    main()