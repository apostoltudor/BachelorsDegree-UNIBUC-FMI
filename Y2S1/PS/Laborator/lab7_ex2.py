import numpy as np
import math

def probabilitate_mai_mult_de_150(lam, threshold):
    log_prob_mai_putin_sau_egal_de_threshold = -lam
    for k in range(1, threshold + 1):
        log_prob_mai_putin_sau_egal_de_threshold += math.log(lam) - math.log(k)
    
    prob_mai_putin_sau_egal_de_threshold = math.exp(log_prob_mai_putin_sau_egal_de_threshold)
    
    prob_mai_mult_de_threshold = 1 - prob_mai_putin_sau_egal_de_threshold
    return prob_mai_mult_de_threshold

def main():
    lam = float(input("rata medie de pacienti pe ora (lambda): "))
    threshold = int(input("pragul de pacienti: "))
    probabilitate = probabilitate_mai_mult_de_150(lam, threshold)
    print(f"probabilitatea ca sa ajunga mai mult de {threshold} pacienti intr-o ora este: {probabilitate:.4f}")

if __name__ == "__main__":
    main()