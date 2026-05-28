import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

date = {
    'masina': ['Golf 7.5 GTD', 'Polo GTI', 'Hyundai IONIQ'],
    'turatii': [2000, 2500, 3000, 3500, 4000, 4500, 5000],
    'consum': [
        [6.5, 5.8, 5.2, 4.9, 4.7, 4.5, 4.3],  # Golf 7.5 GTD
        [7.0, 6.3, 5.7, 5.4, 5.2, 5.0, 4.8],  # Polo GTI
        [4.5, 4.2, 4.0, 3.8, 3.7, 3.6, 3.5]  # Hyundai IONIQ
    ]
}


def analizeaza_date_masina(index_masina):
    nume_masina = date['masina'][index_masina]
    turatii = np.array(date['turatii'])
    consum = np.array(date['consum'][index_masina])

    print(f"date pentru {nume_masina}:")
    for t, c in zip(turatii, consum):
        print(f"turatii: {t}, consum: {c} L/100km")

    covarianta = np.cov(turatii, consum)[0, 1]
    corelatie = np.corrcoef(turatii, consum)[0, 1]
    print(f'\ncovarianta: {covarianta}')
    print(f'corelatie: {corelatie}')

    panta, intersectie, _, _, _ = linregress(turatii, consum)
    print(f'coeficienti regresie liniara: panta = {panta}, intersectie = {intersectie}')

    # (d) Graficul datelor și al liniei de regresie
    plt.figure(figsize=(10, 6))
    plt.scatter(turatii, consum, alpha=0.7, edgecolor='k', label='puncte de date')
    plt.plot(turatii, panta * turatii + intersectie, color='red', label='linie de regresie')
    plt.title(f'{nume_masina}: turatii vs consum')
    plt.xlabel('turatii (RPM)')
    plt.ylabel('consum (L/100km)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # (e) 80% date de antrenament pentru regresie liniară
    marime_antrenament = int(0.8 * len(turatii))
    turatii_antrenament = turatii[:marime_antrenament]
    consum_antrenament = consum[:marime_antrenament]
    turatii_test = turatii[marime_antrenament:]
    consum_test = consum[marime_antrenament:]

    panta_antrenament, intersectie_antrenament, _, _, _ = linregress(turatii_antrenament, consum_antrenament)
    print(
        f'\ncoeficienti regresie liniara pentru 80% date de antrenament: panta = {panta_antrenament}, intersectie = {intersectie_antrenament}')

    consum_predictat = panta_antrenament * turatii_test + intersectie_antrenament

    print("\ncomparatie intre valorile reale si cele prezise pentru restul de 20% din date:")
    for real, prezis in zip(consum_test, consum_predictat):
        print(f'real: {real}, prezis: {prezis}')


def main():
    for i in range(len(date['masina'])):
        analizeaza_date_masina(i)


if __name__ == "__main__":
    main()