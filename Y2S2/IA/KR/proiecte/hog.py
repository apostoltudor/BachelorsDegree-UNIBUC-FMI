import math
import random

GOAL = 100 
WIN_VAL = 10000  


def build_sum_dist(n):
    #distributie sume zaruri fara 1
    dp = {0: 1}
    for _ in range(n):
        ndp = {}
        for s, w in dp.items():
            for f in range(2, 7):
                ndp[s + f] = ndp.get(s + f, 0) + w
        dp = ndp
    total = 5 ** n
    return tuple((s, w / total) for s, w in sorted(dp.items()))


#calc distributii pt zaruir
SDIST = {n: build_sum_dist(n) for n in range(1, 11)}


def free_bacon(opp):
    return 1 + max(opp // 10, opp % 10)


def heuristic(s1, s2):
    #e(s) = 10*diff_scor + 4*diff_fb
    return 10 * (s1 - s2) + 4 * (free_bacon(s2) - free_bacon(s1))


cache = {}


def chance(s1, s2, p1_turn, n, d, dmax):
    if p1_turn:
        plr, opp = s1, s2
    else:
        plr, opp = s2, s1

    if n == 0:
        #free bacon
        pts = free_bacon(opp)
        if p1_turn:
            return search(plr + pts, s2, False, d + 1, dmax)
        return search(s1, plr + pts, True, d + 1, dmax)

    #prob sa fie un 1
    pig = 1.0 - (5.0 / 6.0) ** n
    npig = (5.0 / 6.0) ** n

    #media ponderata a rezultatelor
    if p1_turn:
        ev = pig * search(plr + 1, s2, False, d + 1, dmax)
        for total, prob in SDIST[n]:
            ev += npig * prob * search(plr + total, s2, False, d + 1, dmax)
    else:
        ev = pig * search(s1, plr + 1, True, d + 1, dmax)
        for total, prob in SDIST[n]:
            ev += npig * prob * search(s1, plr + total, True, d + 1, dmax)
#calculeaza un scor general mediu din toate probabilitatile zarurilor
    return ev


def search(s1, s2, p1_turn, d, dmax):
    #expectimax, alege cel mai bun scoir euristic
    if s1 >= GOAL: return WIN_VAL
    if s2 >= GOAL: return -WIN_VAL
    if d >= dmax: return heuristic(s1, s2)

    key = (s1, s2, p1_turn, d)
    if key in cache:
        return cache[key]

    vals = [chance(s1, s2, p1_turn, n, d, dmax) for n in range(11)]

    result = max(vals) if p1_turn else min(vals)
    cache[key] = result
    return result


def pick_best(s1, s2, p1_turn, dmax):
    global cache
    cache = {}

    best_n, best_v = 0, None
    for n in range(11):
        v = chance(s1, s2, p1_turn, n, 0, dmax)
        if best_v is None:
            best_v, best_n = v, n
        elif p1_turn and v > best_v:
            best_v, best_n = v, n
        elif not p1_turn and v < best_v:
            best_v, best_n = v, n
#alege cea mai buna evaluare ev si nr ei n de zaruri ca sa aleaga n
    return best_n


def throw_dice(n):
    dice = [random.randint(1, 6) for _ in range(n)]
    if 1 in dice:
        return 1, dice
    return sum(dice), dice


def ask_player():
    while True:
        r = input("Alege jucatorul 1 sau 2 ").strip()
        if r in ("1", "2"):
            return int(r)
        print("Doar 1 sau 2.")


def ask_dmax():
    while True:
        r = input("Alege dmax: ").strip()
        try:
            v = int(r)
            if v >= 1:
                return v
        except ValueError:
            pass
        print("Numarul trebuie sa fie >=1.")


def play():
    human = ask_player()
    dmax = ask_dmax()
    s1, s2 = 0, 0
    p1_turn = True

    print(f"\nHog - Expectimax (dmax={dmax})")
    print("Primul care are 100 de puncte castiga.\n")

    while s1 < GOAL and s2 < GOAL:
        tag = "J1" if p1_turn else "J2"
        print(f"Tura {tag}")
        print(f"Scor: J1={s1} | J2={s2}")

        is_human = (p1_turn and human == 1) or (not p1_turn and human == 2)

        if is_human:
            while True:
                r = input("Introdu numar zaruri (0-10): ").strip()
                try:
                    n = int(r)
                    if 0 <= n <= 10:
                        break
                except ValueError:
                    pass
                print("Introdu 0-10.")
        else:
            #randul AI-ului
            n = pick_best(s1, s2, p1_turn, dmax)
            print(f"AI alege {n} zaruri.")

        #aplica rezultatul turei
        if n == 0:
            opp = s2 if p1_turn else s1
            pts = free_bacon(opp)
            print(f"Free Bacon: +{pts} puncte")
        else:
            pts, dice = throw_dice(n)
            print(f"Zaruri: {dice}")
            if pts == 1:
                print("Pig Out! +1 punct")
            else:
                print(f"Suma: +{pts} puncte")

        #actualizeaza scorul
        if p1_turn:
            s1 += pts
        else:
            s2 += pts

        print(f"Scor: J1={s1} | J2={s2}\n")
        p1_turn = not p1_turn

    #afiseaza rezultatul final
    print("Joc terminat !!!")
    print(f"Scor final: J1={s1} | J2={s2}")

    if s1 >= GOAL:
        w = 1
    else:
        w = 2

    is_hw = (w == human)
    if is_hw:
        print(f"Jucatorul {w} a castigat! Felicitari!")
    else:
        print(f"Jucatorul {w} (AI) a castigat!")


if __name__ == "__main__":
    play()
