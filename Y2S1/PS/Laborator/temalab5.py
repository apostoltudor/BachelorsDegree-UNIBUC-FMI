import numpy as np
import matplotlib.pyplot as plt

def simuleaza_joc(m, M, numar_simulari=1000000):
    castiguri = []
    durate_jocuri = []

    for _ in range(numar_simulari):
        suma_curenta = m
        durata = 0

        while suma_curenta > 0 and suma_curenta < M:
            if np.random.rand() < 0.5:
                suma_curenta += 10
            else:
                suma_curenta -= 15
            durata += 1

        castiguri.append(suma_curenta >= M)
        durate_jocuri.append(durata)

    prob_castig = np.mean(castiguri)
    return prob_castig, durate_jocuri

def afiseaza_histograma(durate_jocuri):
    plt.hist(durate_jocuri, bins=30, edgecolor='black')
    plt.title('histograma duratei jocurilor')
    plt.xlabel('durata jocului')
    plt.ylabel('frecventa')
    plt.show()

def main():
    m = int(input("suma initiala m (0 < m): "))
    M = int(input("suma dorita M (M > m): "))

    prob_castig, durate_jocuri = simuleaza_joc(m, M)
    print(f"probabilitatea ca jucatorul sa atinga suma de {M} lei este: {prob_castig:.4f}")

    afiseaza_histograma(durate_jocuri)

if __name__ == "__main__":
    main()