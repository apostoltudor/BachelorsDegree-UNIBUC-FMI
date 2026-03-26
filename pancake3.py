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


def ida_star(initial_state):
    #generam pt starea finala
    n = len(initial_state)
    goal_state = tuple(range(1, n + 1))
    
    #setam limitam initiala la h(n) pt startea initala
    bound = gap_heuristic(initial_state)
    
    #retinem doar drumul curent, doar starile de pe drumul actual
    path_states = [initial_state]
    #retine valorile lui k pe drumul actual
    path_moves = []
    
    def search(g, current_bound):
        #ne uitam la ultima stare, cea curenta
        current_state = path_states[-1]
        
        #calculam costul estimat
        f = g + gap_heuristic(current_state)
        
        #daca depaseste limita, ne oprim si returnam costul ce a depasit
        if f > current_bound:
            return f
            
        #daca a ajuns la final, am gasit solutia
        if current_state == goal_state:
            return "FOUND"
            
        #variabila pt a pastra cel mai mic cost ce a depasit limita
        min_bound = float('inf')
        
        #generam mutarile posibile
        for k in range(2, n + 1):
            new_state = flip(current_state, k)
            
            #verificam sa nu fie un ciclu
            if new_state not in path_states:
                #adaugam starea si mutarea
                path_states.append(new_state)
                path_moves.append(k)
                
                #ne uitam mai in adancime cu noua stare si costul crescut cu 1
                t = search(g + 1, current_bound)
                
                #succes
                if t == "FOUND":
                    return "FOUND"
                    
                #daca nu e succes, actualizam limita minima depasita
                if t < min_bound:
                    min_bound = t
                    
                #stergem mutarea curenta pentru a putea explora alta ramura
                path_states.pop()
                path_moves.pop()
                
        return min_bound

    #bucla unde marim limita pana gasim solutia
    while True:
        #cautam in adancime pana la limita curenta
        t = search(0, bound)
        
        #succes
        if t == "FOUND":
            return path_moves, len(path_moves)
            
        #daca t e inf, nu am nu am gasit solutie si nu am depasit limita, deci nu exista solutie
        if t == float('inf'):
            return None, -1
            
        #altfel setam limita la t
        bound = t

if __name__ == "__main__":
    stiva_initiala = (4, 7, 2, 6, 1, 5, 3)
    print(f"Stiva initiala: {stiva_initiala}\n")
    
    mutari_ida, numar_pasi_ida = ida_star(stiva_initiala)
    
    if mutari_ida is not None:
        print(f"Am gasit solutia in {numar_pasi_ida} pasi")
        print(f"Secventa de flip-uri (valorile lui k): {mutari_ida}\n")
    else:
        print("Nu am gasit o solutie")