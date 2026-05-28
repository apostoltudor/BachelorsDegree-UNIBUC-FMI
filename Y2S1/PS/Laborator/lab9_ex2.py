import numpy as np
import matplotlib.pyplot as plt

def importance_sampling_integration(f, a, b, n, lambda_param):
    samples = np.random.exponential(1/lambda_param, n)
    samples = samples[samples <= b]
    f_values = f(samples)
    weights = np.exp(lambda_param * samples) / lambda_param
    integral_approximation = np.mean(f_values / weights) * (b - a)
    return integral_approximation

def plot_integral_approximations(f, a, b, max_n, lambda_param):
    approximations = [importance_sampling_integration(f, a, b, n, lambda_param) for n in range(1, max_n + 1)]
    plt.figure(figsize=(12, 6))
    plt.plot(range(1, max_n + 1), approximations, label='aproximarea integralei')
    plt.title(f'aproximarea integralei in functie de numarul de esantioane')
    plt.xlabel('numarul de esantioane')
    plt.ylabel('aproximarea integralei')
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    f = lambda x: 10 * np.exp(-10 * x) * x**2 * np.sin(x)
    a, b = 0, 100
    lambda_param = 10

    max_n = 1000  

    integral_approximation = importance_sampling_integration(f, a, b, max_n, lambda_param)
    print(f"aproximarea integralei: {integral_approximation}")

    plot_integral_approximations(f, a, b, max_n, lambda_param)

if __name__ == "__main__":
    main()