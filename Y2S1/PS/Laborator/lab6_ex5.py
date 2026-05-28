import numpy as np

def probabilitate_incompatibil_k(p, k):
    prob_incompatibil_k = (1 - p) ** k
    return prob_incompatibil_k

def main():
    p = float(input("probabilitatea sa fie compatibil p: "))
    k = int(input("numarul minim de donatori incompatibili k: "))

    probabilitate = probabilitate_incompatibil_k(p, k)
    print(f"probabilitatea ca pacientul sa fie incompatibil cu cel puțin {k} donatori este: {probabilitate:.4f}")

if __name__ == "__main__":
    main()