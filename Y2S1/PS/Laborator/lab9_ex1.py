import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_integration(f, a, b, n):
    x_random = np.random.uniform(a, b, n)
    f_values = f(x_random)
    average_value = np.mean(f_values)
    integral_approximation = (b - a) * average_value
    return integral_approximation

def plot_function(f, a, b, title):
    x = np.linspace(a, b, 1000)
    y = f(x)
    plt.figure(figsize=(12, 6))
    plt.plot(x, y, label=f'graficul functiei {title}')
    plt.title(f'graficul functiei {title} pe intervalul [{a}, {b}]')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_integral_approximations(f, a, b, max_n):
    approximations = [monte_carlo_integration(f, a, b, n) for n in range(1, max_n + 1)]
    plt.figure(figsize=(12, 6))
    plt.plot(range(1, max_n + 1), approximations, label='aproximarea integralei')
    plt.title(f'aproximarea integralei in functie de numarul de esantioane')
    plt.xlabel('numarul de esantioane')
    plt.ylabel('aproximarea integralei')
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_histogram_of_simulations(f, a, b, n, num_simulations):
    simulations = [monte_carlo_integration(f, a, b, n) for _ in range(num_simulations)]
    plt.figure(figsize=(12, 6))
    plt.hist(simulations, bins=30, alpha=0.5, color='blue', edgecolor='black', density=True)
    plt.title(f'histograma aproximarilor integralei cu {n} esantioane')
    plt.xlabel('aproximarea integralei')
    plt.ylabel('densitate')
    plt.grid(True)
    plt.show()

def main():

    n = 1000
    num_simulations = 100

    plot_function(lambda x: np.exp(-x**2), 0, 1, f"f(x) pe intervalul [0, 1]")

    integral_approximation = monte_carlo_integration(lambda x: np.exp(-x**2), 0, 1, n)
    print(f"aproximarea integralei: {integral_approximation}")

    plot_integral_approximations(lambda x: np.exp(-x**2), 0, 1, n)

    plot_histogram_of_simulations(lambda x: np.exp(-x**2), 0, 1, n, num_simulations)

if __name__ == "__main__":
    main()