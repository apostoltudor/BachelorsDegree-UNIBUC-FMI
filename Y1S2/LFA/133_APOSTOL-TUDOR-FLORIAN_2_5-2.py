dictionar = {}
with open('input.txt') as f:
    for line in f:
        lista = line.split()
        cheie = lista[0]
        dictionar[cheie] = []
        for elem in lista[2::2]:
            dictionar[cheie].append(elem)
n = int(input("n="))
lista = []
cuvant = ""

for cuv in dictionar['S']:
    lista.append(cuv)

while len(cuvant) <= n:

    newlist = []
    for cuv in lista:
        for litera in cuv[::-1]:
            if litera in dictionar.keys():
                for q in dictionar[litera]:
                    cuvant = cuv[:-1] + q
                    newlist.append(cuvant)
    lista = newlist

for cuv in lista:
    if cuv[-1] not in dictionar.keys() and len(cuv) == n:
        print(cuv)