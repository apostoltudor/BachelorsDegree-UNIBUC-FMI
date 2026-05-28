import math

#probabilitatea de a trece mai mult de k masini prin bariera intr-o ora

def probabilitate_mai_mult_de_k(lam, k):
    prob_mai_putin_sau_egal_de_k = sum(math.exp(-lam) * (lam ** i) / math.factorial(i) for i in range(k + 1))

    prob_mai_mult_de_k = 1 - prob_mai_putin_sau_egal_de_k
    return prob_mai_mult_de_k


def main():
    lam = float(input("numarul mediu de masini pe ora: "))
    k = int(input("numarul de masini dorit: "))

    probabilitate = probabilitate_mai_mult_de_k(lam, k)
    print(f"probabilitatea este: {probabilitate:.4f}")


if __name__ == "__main__":
    main()