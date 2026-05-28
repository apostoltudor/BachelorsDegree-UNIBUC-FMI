import heapq

def flip(state, k):
    #luam primele k, le inversam si le unim cu restul
    return state[:k][::-1] + state[k:]


def gap_heuristic(state):
    gaps = 0
    n = len(state)
    
    for i in range(n - 1):
        #le luam in ordine si calculam cate gap-uri avem
        if abs(state[i] - state[i+1]) > 1:
            gaps += 1
            
    #vertificam si baza daca e ce trebuie
    if state[-1] != n:
        gaps += 1
        
    return gaps


def a_star(initial_state):
    n = len(initial_state)
    #generam tupluri pentru starea finala, care e ordonata crescator de la 1 la n, un ideal
    goal_state = tuple(range(1, n + 1)) 
    
    #priority queue va stoca tupluri de forma: f_score, g_score, curent_state, path_to_current_state
    #unde f_score = g_score + h_score
    pq = []
    
    #initializam
    h_start = gap_heuristic(initial_state)
    heapq.heappush(pq, (h_start, 0, initial_state, []))
    
    #set ca sa notam starile pe unde am trecut
    visited = set()
    
    while pq:
        #extragem starea din varful cozii de prioritati (cu cel mai mic f_score)
        f, g, current_state, path = heapq.heappop(pq)
        
        #daca am ajuns la starea finala returnam drumul si nr de pasi
        if current_state == goal_state:
            return path, g
            
        #daca starea curenta a fost deja vizitata, o sarim
        if current_state in visited:
            continue
            
        #punem starea curentam in setul de vizitate
        visited.add(current_state)
        
        #generam toate mutarile posibile
        for k in range(2, n + 1): #fara flip de 1, logic
            new_state = flip(current_state, k)
            
            if new_state not in visited:
                new_g = g + 1
                new_h = gap_heuristic(new_state)
                new_f = new_g + new_h
                new_path = path + [k] #adaugam mutarea k la drumul nostru
                
                #punem noua stare in coada de prioritati
                heapq.heappush(pq, (new_f, new_g, new_state, new_path))
                
    return None, -1

if __name__ == "__main__":
    #vf=4, baza=3
    stiva_initiala = (4, 7, 2, 6, 1, 5, 3)    
    print(f"Stiva initiala: {stiva_initiala}")
    
    mutari, numar_pasi = a_star(stiva_initiala)
    
    if mutari is not None:
        print(f"S-a gasit solutia in {numar_pasi} pasi")
        print(f"Mutarile necesare (valorile lui k pentru flip): {mutari}")
        
        stiva_curenta = stiva_initiala
        #aplicam mutarile ca sa le putem vedea
        for k in mutari:
            stiva_curenta = flip(stiva_curenta, k)
            print(f"Dupa flip({k}): {stiva_curenta}")
    else:
        print("Nu am gasit o solutie")