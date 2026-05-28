import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(2 * x) + 0.3 * np.cos(10 * x) + 0.05 * np.sin(100 * x)

def gaussian_filter_approximation(f, x, sigma, n_samples):
    y_samples = np.random.normal(0, sigma, n_samples)
    f_values = f(x - y_samples)
    weights = np.exp(-y_samples**2 / (2 * sigma**2)) / (np.sqrt(2 * np.pi) * sigma)
    integral_approximation = np.mean(f_values / weights)
    return integral_approximation

def plot_function_and_filter(a, b, sigma_values, n_samples):
    x_values = np.linspace(a, b, 500)
    f_values = f(x_values)

    plt.figure(figsize=(12, 6))
    plt.plot(x_values, f_values, label='f(x)', color='blue')

    for sigma in sigma_values:
        F_values = [gaussian_filter_approximation(f, x, sigma, n_samples) for x in x_values]
        plt.plot(x_values, F_values, label=f'F sigma^2(x) pentru sigma={sigma}', linestyle='--')

    plt.title('graficul functiei f(x) si aproximarea filtrului Gaussian F sigma^2(x)')
    plt.xlabel('x')
    plt.ylabel('Valoare')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    a, b = 0, 5
    n_samples = 1000  
    sigma_values = [1, 0.5, 0.2, 0.1, 0.05]

    x_values = np.linspace(a, b, 500)
    f_values = f(x_values)
    plt.figure(figsize=(12, 6))
    plt.plot(x_values, f_values, label='f(x)', color='blue')
    plt.title('Graficul funcției f(x) pe intervalul [0, 5]')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()

    plot_function_and_filter(a, b, sigma_values, n_samples)

if __name__ == "__main__":
    main()