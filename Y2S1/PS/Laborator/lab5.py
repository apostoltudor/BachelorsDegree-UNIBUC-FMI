import numpy as np

def simuleaza_zaruri_ex1(numar_simulari=100000):
    zar1 = np.random.randint(1, 7, numar_simulari)
    zar2 = np.random.randint(1, 7, numar_simulari)

    a = (zar1 == 1)
    b = (zar2 == 6)
    c = (zar1 + zar2 == 7)

    prob_a = np.mean(a)
    prob_b = np.mean(b)
    prob_c = np.mean(c)
    prob_a_c = np.mean(a & c)
    prob_b_c = np.mean(b & c)
    prob_a_b_c = np.mean(a & b & c)

    return prob_a, prob_b, prob_c, prob_a_c, prob_b_c, prob_a_b_c

def simuleaza_zaruri_ex2(numar_simulari=100000):
    zar1 = np.random.randint(1, 7, numar_simulari)
    zar2 = np.random.randint(1, 7, numar_simulari)

    a = (zar1 <= 2)
    b = (zar1 + zar2 == 7)
    c = (zar2 % 2 == 0)

    prob_a = np.mean(a)
    prob_b = np.mean(b)
    prob_c = np.mean(c)
    prob_a_c = np.mean(a & c)
    prob_b_c = np.mean(b & c)
    prob_a_b = np.mean(a & b)
    prob_a_b_c = np.mean(a & b & c)

    return prob_a, prob_b, prob_c, prob_a_c, prob_b_c, prob_a_b_c, prob_a_b

def simuleaza_zaruri_ex3(numar_simulari=100000):
    zar1 = np.random.randint(1, 7, numar_simulari)
    zar2 = np.random.randint(1, 7, numar_simulari)
    
    a = (zar1 %2 == 1)
    b = (zar1 + zar2 == 4)
    c = (zar2 >= 5)

    prob_a = np.mean(a)
    prob_b = np.mean(b)
    prob_c = np.mean(c)
    prob_a_c = np.mean(a & c)
    prob_b_c = np.mean(b & c)
    prob_a_b = np.mean(a & b)
    prob_a_b_c = np.mean(a & b & c)

    return prob_a, prob_b, prob_c, prob_a_c, prob_b_c, prob_a_b_c, prob_a_b

def independenta_a_ex4(numar_simulari=100000):
    x = np.random.uniform(-1, 2, numar_simulari)
    y = np.random.uniform(-1, 2, numar_simulari)
    
    prob_x_y = np.corrcoef(x, y)[0, 1]

    return prob_x_y

def independenta_b_ex4(numar_simulari=100000):
    x = np.random.uniform(-1, 2, numar_simulari)
    y = -x
    
    prob_x_y = np.corrcoef(x, y)[0, 1]

    return prob_x_y

def simuleaza_joc_ex5(m, M, numar_simulari=10000):
    castiguri = []

    for _ in range(numar_simulari):
        suma_curenta = m

        while suma_curenta > 0 and suma_curenta < M:
            if np.random.rand() < 0.5:
                suma_curenta += 1
            else:
                suma_curenta -= 1
        castiguri.append(suma_curenta >= M)

    prob_castig = np.mean(castiguri)
    return prob_castig

def main():
    x = int(input("exercitiul: "))
    if x == 1:
        prob_a, prob_b, prob_c, prob_a_c, prob_b_c, prob_a_b_c, prob_a_b = simuleaza_zaruri_ex1()
        print(f"a) P(A & C) = {prob_a_c:.4f}, P(A) * P(C) = {prob_a * prob_c:.4f}")
        print(f"b) P(B & C) = {prob_b_c:.4f}, P(B) * P(C) = {prob_b * prob_c:.4f}")
        print(f"c) P(A & B & C) = {prob_a_b_c:.4f}, P(A) * P(B) * P(C) = {prob_a * prob_b * prob_c:.4f}")
    elif x == 2:
        prob_a, prob_b, prob_c, prob_a_c, prob_b_c, prob_a_b_c, prob_a_b = simuleaza_zaruri_ex2()
        print(f"a) P(A & C) = {prob_a_c:.4f}, P(A) * P(C) = {prob_a * prob_c:.4f}")
        print(f"b) P(A & B) = {prob_a_b:.4f}, P(A) * P(B) = {prob_a * prob_b:.4f}")
        print(f"c) P(B & C) = {prob_b_c:.4f}, P(B) * P(C) = {prob_b * prob_c:.4f}")
        print(f"d) P(A & B & C) = {prob_a_b_c:.4f}, P(A) * P(B) * P(C) = {prob_a * prob_b * prob_c:.4f}")
    elif x == 3:
        prob_a, prob_b, prob_c, prob_a_c, prob_b_c, prob_a_b_c, prob_a_b = simuleaza_zaruri_ex3()
        print(f"a) P(A & C) = {prob_a_c:.4f}, P(A) * P(C) = {prob_a * prob_c:.4f}") #a independent de c
        print(f"b) P(B & C) = {prob_b_c:.4f}, P(B) * P(C) = {prob_b * prob_c:.4f}") #b independent de c
        print(f"c) P(A & B & C) = {prob_a_b_c:.4f}, P(A) * P(B) * P(C) = {prob_a * prob_b * prob_c:.4f}") #a b si c indeprndente
    elif x == 4:
        print(f"a) prob_x_y = {independenta_a_ex4():.4f}")
        print(f"b) prob_x_y = {independenta_b_ex4():.4f}")
    elif x == 5:
        m = int(input("suma inițială (m): "))
        M = int(input("suma dorită (M): "))
        prob_castig = simuleaza_joc_ex5(m, M)
        print(f"probabilitatea sa se atinga suma M ({M}) este: {prob_castig:.4f}")
    else:
        print(f"nu exista exercitiul {x}")

if __name__ == "__main__":
    main()