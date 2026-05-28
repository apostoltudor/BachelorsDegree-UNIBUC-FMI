#ex2 PARADOXUL ZILEI DE NASTERE

#a)
import numpy as np


def birthday_simulation(num_people, num_simulations):

    collision_count = 0

    for _ in range(num_simulations):
        birthdays = np.random.randint(0, 365, num_people)

        if len(birthdays) != len(set(birthdays)):
            collision_count += 1

    probability = collision_count / num_simulations
    return probability


num_people = 23
num_simulations = 100000

estimated_probability = birthday_simulation(num_people, num_simulations)

print(
    f'Probabilitatea ca dintr-un grup de {num_people} persoane, cel puțin două să aibă aceeași zi de naștere: {estimated_probability:.4f}')

#b)

