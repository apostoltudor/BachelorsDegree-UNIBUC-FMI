import numpy as np

def probabilitate_asteptare_mai_mult_de(lam, t):
    return np.exp(-lam * t)

def main():
    avg_arrival_tram = float(input("timpul mediu de sosire al tramvaiului: "))
    avg_arrival_bus = float(input("timpul mediu de sosire al autobuzului: "))

    lam_tram = 1 / avg_arrival_tram
    lam_bus = 1 / avg_arrival_bus

    t = 5

    prob_tram = probabilitate_asteptare_mai_mult_de(lam_tram, t)
    print(f"probabilitatea de a astepta mai mult de {t} minute tramvaiul: {prob_tram:.4f}")

    prob_bus = probabilitate_asteptare_mai_mult_de(lam_bus, t)
    prob_tram_sau_bus = prob_tram * prob_bus
    print(f"probabilitatea de a astepta mai mult de {t} minute tramvaiul sau autobuzul: {prob_tram_sau_bus:.4f}")

if __name__ == "__main__":
    main()