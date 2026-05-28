import numpy as np
import math

def probabilitate_cel_putin_k(n, p, k):
    prob_mai_putin_de_k = sum(math.comb(n, i) * (p**i) * ((1-p)**(n-i)) for i in range(k))
    prob_cel_putin_k = 1 - prob_mai_putin_de_k
    return prob_cel_putin_k

def main():
    n = int(input("n: "))
    p = float(input("p: "))
    k = int(input("k: "))

    if k > n:
        print("k <= n")
        return

    probabilitate = probabilitate_cel_putin_k(n, p, k)
    print(f"probabilitatea ca cel putin {k} oameni sa fie angajati este: {probabilitate:.4f}")

if __name__ == "__main__":
    main()