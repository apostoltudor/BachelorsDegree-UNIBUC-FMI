import numpy as np

def probabilitate_mai_mult_de(lam, t):
    prob_mai_mult_de_t = np.exp(-lam * t)
    return prob_mai_mult_de_t

def main():
    durata_medie_telefon1 = float(input("durata medie de funcționare a telefonului 1 (ani): "))
    durata_medie_telefon2 = float(input("durata medie de funcționare a telefonului 2 (ani): "))

    lam_telefon1 = 1 / durata_medie_telefon1
    lam_telefon2 = 1 / durata_medie_telefon2

    probabilitate_telefon1 = probabilitate_mai_mult_de(lam_telefon1, durata_medie_telefon1)
    probabilitate_telefon2 = probabilitate_mai_mult_de(lam_telefon2, durata_medie_telefon2)

    print(f"probabilitatea ca telefonul 1 sa functioneze mai mult de {durata_medie_telefon1} ani este: {probabilitate_telefon1:.4f}")
    print(f"probabilitatea ca telefonul 2 sa functioneze mai mult de {durata_medie_telefon2} ani este: {probabilitate_telefon2:.4f}")

if __name__ == "__main__":
    main()