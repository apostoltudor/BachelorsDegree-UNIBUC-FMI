import numpy as np
import matplotlib.pyplot as plt

def simulate_trajectory(n, step_values, probabilities):
    steps = np.random.choice(step_values, size=n, p=probabilities)
    trajectory = np.cumsum(np.insert(steps, 0, 0))  # Start from 0
    return trajectory

def simulate_final_positions(n, num_simulations, step_values, probabilities):
    final_positions = []
    for _ in range(num_simulations):
        steps = np.random.choice(step_values, size=n, p=probabilities)
        final_position = np.sum(steps)
        final_positions.append(final_position)
    return final_positions

def plot_trajectory(trajectory):
    plt.figure(figsize=(12, 6))
    plt.plot(trajectory, label='traiectorie')
    plt.title('traiectoria mersului aleator')
    plt.xlabel('pasi')
    plt.ylabel('pozitie')
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_histogram(final_positions):
    plt.figure(figsize=(12, 6))
    plt.hist(final_positions, bins=50, alpha=0.5, color='blue', edgecolor='black', density=True, label='histograma pozitii finale')
    plt.title('histograma pozitii finale dupa n pași')
    plt.xlabel('pozitie finala')
    plt.ylabel('densitate')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    n = int(input("numarul de pasi n: "))
    num_simulations = int(input("numarul de simulari: "))

    step_values = [-2, 0, 1]
    probabilities = [0.2, 0.5, 0.3]

    trajectory = simulate_trajectory(n, step_values, probabilities)
    plot_trajectory(trajectory)

    final_positions = simulate_final_positions(n, num_simulations, step_values, probabilities)

    plot_histogram(final_positions)

if __name__ == "__main__":
    main()