#ex 1
import numpy as np

print("ex 1:")

def simuleaza_teste_boala(nr_simulari=1000000):
    prob_b = 0.02
    precizie_poz = 0.98
    precizie_neg = 0.95

    nr_poz = 0
    nr_boala_si_poz = 0
    nr_dublu_poz = 0
    nr_boala_si_dublu_poz = 0

    for _ in range(nr_simulari):
        are_boala = np.random.rand() < prob_b
        rezultat_test1 = (np.random.rand() < precizie_poz) if are_boala else (np.random.rand() < (1 - precizie_neg))
        rezultat_test2 = (np.random.rand() < precizie_poz) if are_boala else (np.random.rand() < (1 - precizie_neg))

        if rezultat_test1:
            nr_poz += 1
            if are_boala:
                nr_boala_si_poz += 1

        if rezultat_test1 and rezultat_test2:
            nr_dublu_poz += 1
            if are_boala:
                nr_boala_si_dublu_poz += 1

    prob_b_daca_poz = nr_boala_si_poz / nr_poz if nr_poz > 0 else 0
    prob_b_daca_dublu_poz = nr_boala_si_dublu_poz / nr_dublu_poz if nr_dublu_poz > 0 else 0

    return prob_b_daca_poz, prob_b_daca_dublu_poz

def main1():
    prob_b_daca_poz, prob_b_daca_dublu_poz = simuleaza_teste_boala()
    print(f"a) {prob_b_daca_poz:.4f}")
    print(f"b) {prob_b_daca_dublu_poz:.4f}")

if __name__ == "__main__":
    main1()
    

#ex 2
import numpy as np

print("ex 2:")

def simuleaza_emailuri(nr_simulari=100000):
    prob_spam = 0.20
    prob_cuv_spam = 0.80
    prob_cuv_non_spam = 0.15

    nr_cuv = 0
    nr_spam_si_cuv = 0

    for _ in range(nr_simulari):
        este_spam = np.random.rand() < prob_spam
        contine_cuv = (np.random.rand() < prob_cuv_spam) if este_spam else (np.random.rand() < prob_cuv_non_spam)

        if contine_cuv:
            nr_cuv += 1
            if este_spam:
                nr_spam_si_cuv += 1

    prob_spam_daca_cuv = nr_spam_si_cuv / nr_cuv if nr_cuv > 0 else 0

    return prob_spam_daca_cuv

def main2():
    prob_spam_daca_cuv = simuleaza_emailuri()
    print(f"a) probabilitatea sa fie spam: {prob_spam_daca_cuv:.4f}")

    if prob_spam_daca_cuv > 0.50:
        print("b) emailul este spam")
    else:
        print("b) emailul nu este spam")

if __name__ == "__main__":
    main2()

