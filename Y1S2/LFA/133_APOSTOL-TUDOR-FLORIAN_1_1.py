with open("input.txt") as automat:
    nr_stari = int(automat.readline())

    lista_stari = automat.readline().split()

    nr_litere = int(automat.readline())

    lista_litere = automat.readline().split()

    stare_initiala = automat.readline().strip()

    nr_stari_finale = int(automat.readline())

    lista_stari_finale = automat.readline().split()

    nr_tranzitii = int(automat.readline())

    lista_tranzitii = []

    for i in range(nr_tranzitii):
        lista_tranzitii.append(automat.readline().split())

    nr_cuvinte = int(automat.readline())

    lista_cuvinte = []

    for i in range(nr_cuvinte):
        linie = automat.readline().split()
        for cuv in linie:
            lista_cuvinte.append(cuv)


def verifica_cuvant(cuv, curenta, sageti, finala):
    for litera in cuv:
        ok = False
        for sageata in sageti:
            if sageata[0] == curenta and sageata[1] == litera:
                curenta = sageata[2]
                ok = True
                break
        if not ok:
            return False
    return curenta in finala


for cuvant in lista_cuvinte:
    if verifica_cuvant(cuvant, stare_initiala, lista_tranzitii, lista_stari_finale):
        print("DA")
    else:
        print("NU")


