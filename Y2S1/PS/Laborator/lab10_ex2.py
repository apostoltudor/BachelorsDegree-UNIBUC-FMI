import numpy as np
import matplotlib.pyplot as plt
from pydataset import data
from scipy.stats import linregress

def plot_and_analyze(nume_set_date, coloana_x, coloana_y, titlu, eticheta_x, eticheta_y):
    df = data(nume_set_date)
    x = df[coloana_x].values
    y = df[coloana_y].values
    
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, alpha=0.7, edgecolor='k', label='puncte de date')
    plt.title(titlu)
    plt.xlabel(eticheta_x)
    plt.ylabel(eticheta_y)
    
    covarianta = np.cov(x, y)[0, 1]
    corelatie = np.corrcoef(x, y)[0, 1]
    print(f'{titlu}:')
    print(f'covarianta: {covarianta}')
    print(f'corelatie: {corelatie}')
    
    panta, intersectie, _, _, _ = linregress(x, y)
    print(f'coeficienti regresie liniara: panta = {panta}, intersectie = {intersectie}')
    
    plt.plot(x, panta * x + intersectie, color='red', label='linie de regresie')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return panta, intersectie

def main():
    plot_and_analyze('iris', 'Sepal.Length', 'Petal.Length', 
                     'iris: lungime sepala vs lungime petala', 'lungime sepala', 'lungime petala')
    
    plot_and_analyze('trees', 'Girth', 'Height', 
                     'copaci: circumferinta vs inaltime', 'circumferinta', 'inaltime')
    
    panta, intersectie = plot_and_analyze('women', 'height', 'weight', 
                                          'femei: inaltime vs greutate', 'inaltime', 'greutate')
    
    df_femei = data('women')
    marime_antrenament = int(0.8 * len(df_femei))
    date_antrenament = df_femei[:marime_antrenament]
    date_test = df_femei[marime_antrenament:]
    
    panta_antrenament, intersectie_antrenament, _, _, _ = linregress(date_antrenament['height'], date_antrenament['weight'])
    print(f'\ncoeficienti regresie liniara pentru 80% date de antrenament: panta = {panta_antrenament}, intersectie = {intersectie_antrenament}')
    
    inaltimi_test = date_test['height']
    greutati_test = date_test['weight']
    greutati_predictate = panta_antrenament * inaltimi_test + intersectie_antrenament
    
    print("\ncomparatie intre greutati reale si cele predictate pentru restul de 20% din date:")
    for reala, prezisa in zip(greutati_test, greutati_predictate):
        print(f'reala: {reala}, prezisa: {prezisa}')

if __name__ == "__main__":
    main()