import numpy as np
import matplotlib.pyplot as plt
def ex1():
    def simulate_coin_flip(num_flips):
        cap_count = 0

        for _ in range(num_flips):
            random_value = np.random.uniform(0, 1)
            if random_value < 0.5:
                cap_count += 1

        probability_heads = cap_count / num_flips
        return probability_heads

    num_flips = 10000

    probability_of_heads = simulate_coin_flip(num_flips)

    print(f'probabilitatea de "heads" după {num_flips} aruncari: {probability_of_heads:.4f}')

def ex3():
    simulations = 100000
    nr = 0

    for _ in range(simulations):
        sequence = ''.join(np.random.choice(['H', 'T'], size=10))  #size = 20 pentru b)   size = 100 pentru c)

        if 'HHHH' in sequence or 'TTTT' in sequence:   # HHHHHHHH sau TTTTTTTT pentru c)
            nr += 1

    probability = nr / simulations
    print(f"probabilitatea estimata este: {probability:.4f}")


def ex4(num_simulations=10000):
    def roll_red_dice():
        return 4 if np.random.rand() > 0.83 else 1

    def roll_green_dice():
        return 3 if np.random.rand() > 0.83 else 6

    def roll_black_dice():
        return 2 if np.random.rand() > 0.5 else 5

    def simulate_battles(num_simulations):
        red_vs_green_wins = 0
        red_vs_black_wins = 0
        black_vs_green_wins = 0

        for _ in range(num_simulations):
            red = roll_red_dice()
            green = roll_green_dice()
            black = roll_black_dice()

            if red > green:
                red_vs_green_wins += 1
            if red > black:
                red_vs_black_wins += 1
            if black > green:
                black_vs_green_wins += 1

        return red_vs_green_wins, red_vs_black_wins, black_vs_green_wins

    red_vs_green_wins, red_vs_black_wins, black_vs_green_wins = simulate_battles(num_simulations)

    print(f'Rosu > Verde: {red_vs_green_wins/num_simulations:.4f}')
    print(f'Rosu > Negru: {red_vs_black_wins/num_simulations:.4f}')
    print(f'Verde > Rosu: {1 - red_vs_green_wins/num_simulations:.4f}')
    print(f'Verde > Negru: {1 - black_vs_green_wins/num_simulations:.4f}')
    print(f'Negru > Rosu: {1 - red_vs_black_wins/num_simulations:.4f}')
    print(f'Negru > Verde: {black_vs_green_wins/num_simulations:.4f}')




