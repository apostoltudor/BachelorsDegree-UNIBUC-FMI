import numpy as np

#probabilitatea ca un bec sa reziste mai mult decat durata medie de viata
def probabilitate_mai_mult_de_t(lam, t):
    return np.exp(-lam * t)

def main():
    avg_lifetime = float(input("durata medie de viata a becului: "))
    
    lam = 1 / avg_lifetime

    t = float(input("durata de viata dorita: "))

    probabilitate = probabilitate_mai_mult_de_t(lam, t)
    print(f"probabilitatea este: {probabilitate:.4f}")

if __name__ == "__main__":
    main()