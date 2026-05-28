import numpy as np
import matplotlib.pyplot as plt


def metoda_a(miu, sigma):
    U1 = np.random.uniform(0, 1)
    U2 = np.random.uniform(0, 1)
    return miu + np.sqrt(-2 * (sigma ** 2) * np.log(U1)) * np.cos(2 * np.pi * U2)


def metoda_b(miu, sigma):
    U1 = np.random.uniform(0, 1)
    U2 = np.random.uniform(0, 1)
    return miu + np.sqrt(-2 * (sigma ** 2) * np.log(U1)) * np.sin(2 * np.pi * U2)


def metoda_c(miu, sigma):
    return np.random.normal(miu, sigma)


def simuleaza_si_afiseaza(miu, sigma, N):
    rezultate_a = [metoda_a(miu, sigma) for _ in range(N)]
    rezultate_b = [metoda_b(miu, sigma) for _ in range(N)]
    rezultate_c = [metoda_c(miu, sigma) for _ in range(N)]

    plt.hist(rezultate_a, bins=50, alpha=0.6, label="metoda a)", density=True)
    plt.hist(rezultate_b, bins=50, alpha=0.6, label="metoda b)", density=True)
    plt.hist(rezultate_c, bins=50, alpha=0.6, label="metoda c)", density=True)

    plt.title("histograma")
    plt.xlabel("valoare")
    plt.ylabel("frecventa relativa")
    plt.legend()
    plt.show()

    return rezultate_a, rezultate_b, rezultate_c


def main():
    miu = 0  
    sigma = 1  
    N = 10000

    rezultate_a, rezultate_b, rezultate_c = simuleaza_si_afiseaza(miu, sigma, N)

    for metoda, rezultate in zip(["a)", "b)", "c)"], [rezultate_a, rezultate_b, rezultate_c]):
        media = np.mean(rezultate)
        varianta = np.var(rezultate)
        print(f"metoda {metoda}: media = {media:.4f}, varianta estimata = {varianta:.4f}")


if __name__ == "__main__":
    main()
