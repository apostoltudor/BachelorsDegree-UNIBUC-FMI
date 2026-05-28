# DFA 1
Q_A = ['A', 'B']
Sigma_A = ['0', '1']
delta_A = {('A', '0'): 'A', ('A', '1'): 'B', ('B', '0'): 'B', ('B', '1'): 'B'}
q0_A = 'A'
F_A = ['B']

# DFA 2
Q_B = ['X', 'Y']
Sigma_B = ['0', '1']
delta_B = {('X', '0'): 'Y', ('X', '1'): 'X', ('Y', '0'): 'Y', ('Y', '1'): 'Y'}
q0_B = 'X'
F_B = ['X']

# Construirea DFA-ului Reuniune
Q_Reuniune = [(qa, qb) for qa in Q_A for qb in Q_B]
Sigma_Reuniune = list(set(Sigma_A + Sigma_B))  # Presupunem că ambele automate folosesc același alfabet
q0_Reuniune = (q0_A, q0_B)
F_Reuniune = [(qa, qb) for qa in Q_A for qb in Q_B if qa in F_A or qb in F_B]

# Funcția de tranziție a DFA-ului Reuniune
delta_Reuniune = {}
for state in Q_Reuniune:
    for letter in Sigma_Reuniune:
        delta_Reuniune[(state, letter)] = (delta_A[(state[0], letter)], delta_B[(state[1], letter)])

# Functie pentru a verifica daca un cuvant este acceptat de DFA-ul Reuniune
def accepta_cuvant_dfa_reuniune(cuvant, stare_curenta, delta, stari_finale):
    for litera in cuvant:
        stare_curenta = delta[(stare_curenta, litera)]
    return stare_curenta in stari_finale

# Testarea cu un cuvant
cuvant_test = '01'
stare_initiala_reuniune = q0_Reuniune
este_acceptat = accepta_cuvant_dfa_reuniune(cuvant_test, stare_initiala_reuniune, delta_Reuniune, F_Reuniune)
print("DA" if este_acceptat else "NU")

#Acest cod definește două automate DFA și apoi construiește un nou DFA care recunoaște reuniunea limbajelor acestora.
# Funcția accepta_cuvant_dfa_reuniune verifică dacă un cuvânt este acceptat de noul DFA. La final,
# testăm cu un cuvânt '01' să vedem dacă este acceptat de DFA-ul reuniune.

#Cum putem verifica dacă un cuvânt este acceptat de DFA-ul Reuniune?

# Pentru a verifica dacă un cuvânt este acceptat de DFA-ul Reuniune, trebuie să urmărim tranzițiile stărilor în DFA pe măsură ce citim fiecare literă a cuvântului de la starea inițială până la finalul cuvântului. Dacă starea la care ajungem după ce am procesat toate literele cuvântului este una dintre stările finale, atunci cuvântul este acceptat de DFA; dacă nu, cuvântul este respins.
#
# Codul Python de mai jos efectuează această verificare:

# def accepta_cuvant_dfa_reuniune(cuvant, stare_curenta, delta, stari_finale):
#     for litera in cuvant:
#         stare_curenta = delta[(stare_curenta, litera)]  # Urmărește tranziția pentru litera curentă
#     return stare_curenta in stari_finale  # Verifică dacă starea finală este una dintre stările finale
#
# # Exemplu de utilizare:
# cuvant_test = '01'  # Cuvântul pe care vrem să îl testăm
# stare_initiala_reuniune = q0_Reuniune  # Starea inițială a DFA-ului Reuniune
# este_acceptat = accepta_cuvant_dfa_reuniune(cuvant_test, stare_initiala_reuniune, delta_Reuniune, F_Reuniune)
# print("DA" if este_acceptat else "NU")

# Funcția accepta_cuvant_dfa_reuniune ia ca argumente cuvântul de testat, starea inițială a DFA-ului Reuniune, funcția de tranziție delta și setul de stări finale. Ea parcurge fiecare literă a cuvântului, actualizând starea curentă folosind funcția de tranziție. Dacă starea curentă după procesarea tuturor literelor este una dintre stările finale, funcția returnează adevărat (indicând că cuvântul este acceptat); altfel, returnează fals (indicând că cuvântul este respins).
#
# Pentru a rula acest cod, asigură-te că ai definit toate variabilele necesare (delta_Reuniune, q0_Reuniune, F_Reuniune) și că funcția de tranziție delta_Reuniune este complet definită pentru toate combinațiile posibile de stări și litere din alfabet.