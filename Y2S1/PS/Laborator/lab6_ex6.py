import numpy as np

def probabilitate_cel_putin_k_flips(p, k):
    prob_cel_putin_k = (1 - p) ** (k - 1)
    return prob_cel_putin_k

def main():
    p = float(input("probabilitatea de a obtine Head p: "))
    k = int(input("numarul minim de aruncari pentru a obține primul Head k: "))

    probabilitate = probabilitate_cel_putin_k_flips(p, k)
    print(f"probabilitatea ca sa fie nevoie de cel putin {k} aruncari pentru a obtine primul Head este: {probabilitate:.4f}")

if __name__ == "__main__":
    main()