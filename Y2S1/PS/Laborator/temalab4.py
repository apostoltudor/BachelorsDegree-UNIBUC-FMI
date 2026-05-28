import numpy as np

#calculeaza probabilitatea ca un client sa cumpere un produc dupa ce
#a dat click pe reclama produsului respectiv
def simuleaza_evenimente(nr_simulari=100000):
    #informatii despre P(A|B)
    prob_a = 0.05 #prob ca un client sa cumpere produsul
    prob_b_daca_a = 0.70 #prob ca un client sa dea click pe reclama daca va cumpara produsul
    prob_b_daca_non_a = 0.10 #prob ca un client sa dea click pe reclama daca nu va cumpara produsul

    numar_b = 0 #numarul de clienti care au dat click pe reclama
    numar_a_si_b = 0 #numarul de clienti care au dat click pe reclama si au cumparat produsul

    for _ in range(nr_simulari):
        cumpara_produs = np.random.rand() < prob_a
        da_click = (np.random.rand() < prob_b_daca_a) if cumpara_produs else (np.random.rand() < prob_b_daca_non_a)

        if da_click:
            numar_b += 1
            if cumpara_produs:
                numar_a_si_b += 1

    prob_a_daca_b = numar_a_si_b / numar_b if numar_b > 0 else 0

    return prob_a_daca_b

def principal():
    prob_a_daca_b = simuleaza_evenimente()
    print(f"probabilitatea ca un client sa cumpere produsul, dupa ce a dat click pe reclama: {prob_a_daca_b:.4f}")

if __name__ == "__main__":
    principal()