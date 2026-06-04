import math
import copy

EMPTY = 0
BLACK = 1 #max
WHITE = -1 #min

DIRS = [
    (0, 1), (1, 0), (0, -1), (-1, 0),
    (1, 1), (-1, -1), (1, -1), (-1, 1)
]

#colturile valoroase
CORNERS = [(0, 0), (0, 7), (7, 0), (7, 7)]
DANGEROUS = [
    (1, 1), (1, 6), (6, 1), (6, 6),       #patrate adiacente colturilor
    (0, 1), (1, 0), (0, 6), (1, 7),       
    (6, 0), (7, 1), (6, 7), (7, 6)
]


def initial_board():
    board = [[EMPTY] * 8 for _ in range(8)]
    board[3][3], board[4][4] = WHITE, WHITE
    board[3][4], board[4][3] = BLACK, BLACK
    return board


def print_board(board):
    print("  " + " ".join(str(i) for i in range(8)))
    for r in range(8):
        row = []
        for c in range(8):
            if board[r][c] == BLACK:
                row.append("B")
            elif board[r][c] == WHITE:
                row.append("W")
            else:
                row.append("_")
        print(f"{r} " + " ".join(row))
    print()


def on_board(r, c):
    return r in range(8) and c in range(8)


def _check_dir(board, r, c, dr, dc, player):
    nr, nc = r + dr, c + dc
    cnt = 0 
    while on_board(nr, nc) and board[nr][nc] == -player:
        nr, nc = nr + dr, nc + dc
        cnt += 1
    return cnt > 0 and on_board(nr, nc) and board[nr][nc] == player


def valid_moves(board, player):
    result = []
    for r in range(8):
        for c in range(8):
            if board[r][c] != EMPTY:
                continue
            #cauta cel putin o directie valida
            for dr, dc in DIRS:
                if _check_dir(board, r, c, dr, dc, player):
                    result.append((r, c))
                    break
    return result


def _get_flips(board, r, c, dr, dc, player):
    captured = []
    nr, nc = r + dr, c + dc
    #aduna piese adversar
    while on_board(nr, nc) and board[nr][nc] == -player:
        captured.append((nr, nc))
        nr, nc = nr + dr, nc + dc
    #verifica daca sunt piese proprii la capat
    if captured and on_board(nr, nc) and board[nr][nc] == player:
        return captured
    return []

def make_move(board, move, player):
    state = copy.deepcopy(board)
    r, c = move
    state[r][c] = player
    #proceseaza directiile
    for dr, dc in DIRS:
        for fr, fc in _get_flips(board, r, c, dr, dc, player):
            state[fr][fc] = player
    return state


def game_ended(board):
    return len(valid_moves(board, BLACK)) == 0 and len(valid_moves(board, WHITE)) == 0


def final_score(board):
    black_count = sum(row.count(BLACK) for row in board)
    white_count = sum(row.count(WHITE) for row in board)
    return black_count, white_count


def heuristic_eval(board):
    #ponderile
    W_CORNER, W_MOBIL, W_DISC, W_RISK = 25, 5, 1, 8

    p1_corners = sum(1 for pos in CORNERS if board[pos[0]][pos[1]] == BLACK)
    p2_corners = sum(1 for pos in CORNERS if board[pos[0]][pos[1]] == WHITE)

    p1_moves = len(valid_moves(board, BLACK))
    p2_moves = len(valid_moves(board, WHITE))

    p1_discs = sum(cell == BLACK for row in board for cell in row)
    p2_discs = sum(cell == WHITE for row in board for cell in row)

    p1_risk = sum(1 for pos in DANGEROUS if board[pos[0]][pos[1]] == BLACK)
    p2_risk = sum(1 for pos in DANGEROUS if board[pos[0]][pos[1]] == WHITE)

    #scor ponderat
    return (W_CORNER * (p1_corners - p2_corners)
          + W_MOBIL  * (p1_moves - p2_moves)
          + W_DISC   * (p1_discs - p2_discs)
          + W_RISK   * (p2_risk - p1_risk))


def alphabeta_search(board, depth, alpha, beta, current_player, dmax):
    INF = 10 ** 9

    #caz terminal: scor real
    if game_ended(board):
        sc_b, sc_w = final_score(board)
        if sc_b > sc_w:   return  INF, None
        elif sc_w > sc_b: return -INF, None
        return 0, None

    #limita adancime
    if depth >= dmax:
        return heuristic_eval(board), None

    options = valid_moves(board, current_player)

    #daca nu are optiuni pass
    if not options:
        score, _ = alphabeta_search(board, depth + 1, alpha, beta, -current_player, dmax)
        return score, None

    is_max = (current_player == BLACK)
    best = -math.inf if is_max else math.inf
    chosen = None

    for mv in options:
        child_board = make_move(board, mv, current_player)
        score, _ = alphabeta_search(child_board, depth + 1, alpha, beta, -current_player, dmax)

        #actualizeaza best si limita
        if is_max and score > best:
            best, chosen = score, mv
            alpha = max(alpha, best)
        elif not is_max and score < best:
            best, chosen = score, mv
            beta = min(beta, best)

        #conditie de taiere ; 50 pe N, daca e pe S 20 stop
        if beta <= alpha:
            break

    return best, chosen


def choose_human_color():
    while True:
        s = input("Alege culoarea B/W: ").strip().upper()
        if s == "B":
            return BLACK
        if s == "W":
            return WHITE
        print("Introdu B sau W.")


def choose_dmax():
    while True:
        s = input("Alege dmax: ").strip()
        try:
            dmax = int(s)
            if dmax >= 1:
                return dmax
        except ValueError:
            pass
        print("Trebuie un numar intreg >= 1.")


def play_game():
    board = initial_board()
    human_player = choose_human_color()
    ai_player = -human_player
    dmax = choose_dmax()
    current_player = BLACK

    print("\nOthello - Minimax cu Alpha-Beta Pruning")
    print("Jucatorul 1 (BLACK) muta primul.\n")

    while not game_ended(board):
        print_board(board)
        moves = valid_moves(board, current_player)

        #jucatorul curent paseaza tura
        if not moves:
            label = "B" if current_player == BLACK else "W"
            print(f"Jucatorul {label} nu are mutari valide si paseaza.\n")
            current_player = -current_player
            continue

        if current_player == human_player:
            print(f"Mutari valide: {moves}")
            move_str = input("Mutarea (r c) sau q (quit): ").strip().lower()

            if move_str == "q":
                print("Joc oprit.")
                return

            try:
                r, c = map(int, move_str.split())
                if (r, c) not in moves:
                    print("Mutare invalida, incearca din nou.\n")
                    continue
                board = make_move(board, (r, c), current_player)
            except ValueError:
                print("Format invalid, foloseste: rand coloana.\n")
                continue
        else:
            #tura AI
            _, move = alphabeta_search(board, 0, -math.inf, math.inf, current_player, dmax)
            print(f"AI muta la: {move}\n")
            board = make_move(board, move, current_player)

        #schimba jucatorul curent
        current_player = -current_player

    #afiseaza rezultat
    print("Joc terminat !!!")
    print_board(board)

    black_count, white_count = final_score(board)
    print(f"Scor final - BLACK: {black_count} | WHITE: {white_count}")

    if human_player == BLACK:
        human_score, ai_score = black_count, white_count
    else:
        human_score, ai_score = white_count, black_count

    if human_score > ai_score:
        print("Felicitari, ai castigat!")
    elif ai_score > human_score:
        print("AI-ul a castigat!")
    else:
        print("Egalitate!")


if __name__ == "__main__":
    play_game()