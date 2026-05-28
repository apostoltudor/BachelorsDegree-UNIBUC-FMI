import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gammaln
from scipy.optimize import minimize

def log_likelihood_neg_binom(data, theta1, theta2):
    n = len(data)
    term1 = np.sum(gammaln(data + theta1))
    term2 = n * gammaln(theta1)
    term3 = np.sum(gammaln(data + 1))
    term4 = np.log(1 - theta2) * np.sum(data)
    term5 = n * theta1 * np.log(theta2)
    return term1 - term2 - term3 + term4 + term5

def log_likelihood_gamma(data, theta1, theta2):
    n = len(data)
    term1 = n * theta1 * np.log(theta2)
    term2 = n * gammaln(theta1)
    term3 = (theta1 - 1) * np.sum(np.log(data))
    term4 = theta2 * np.sum(data)
    return term1 - term2 + term3 - term4

def plot_histogram(data, title):
    plt.figure()
    plt.hist(data, bins=30, alpha=0.7, color='blue')
    plt.title(f'histogram of {title}')
    plt.xlabel('value')
    plt.ylabel('frequenxy')
    plt.show()

def plot_log_likelihood(data, log_likelihood_func, theta1_range, theta2_range, title):
    theta1, theta2 = np.meshgrid(theta1_range, theta2_range)
    log_likelihood = np.zeros_like(theta1)

    for i in range(theta1.shape[0]):
        for j in range(theta1.shape[1]):
            log_likelihood[i, j] = log_likelihood_func(data, theta1[i, j], theta2[i, j])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(theta1, theta2, log_likelihood, cmap='viridis')
    ax.set_title(f'log-likelihood function for {title}')
    ax.set_xlabel('theta1')
    ax.set_ylabel('theta2')
    ax.set_zlabel('log L')
    plt.show()

def find_max_likelihood(data, log_likelihood_func, theta1_range, theta2_range):
    def neg_log_likelihood(params):
        return -log_likelihood_func(data, params[0], params[1])

    initial_guess = [np.mean(theta1_range), np.mean(theta2_range)]
    bounds = [(min(theta1_range), max(theta1_range)), (min(theta2_range), max(theta2_range))]
    result = minimize(neg_log_likelihood, initial_guess, bounds=bounds)
    return result.x

def main():
    data_neg_binom = np.load('sample_NegativBinom.npy')
    data_gamma = np.load('sample_Gamma.npy')

    plot_histogram(data_neg_binom, 'negative binomial data')
    theta1_range = np.linspace(0.1, 10, 100)
    theta2_range = np.linspace(0.01, 0.99, 100)
    plot_log_likelihood(data_neg_binom, log_likelihood_neg_binom, theta1_range, theta2_range, 'negative binomial')

    theta1_hat, theta2_hat = find_max_likelihood(data_neg_binom, log_likelihood_neg_binom, theta1_range, theta2_range)
    log_likelihood_hat = log_likelihood_neg_binom(data_neg_binom, theta1_hat, theta2_hat)
    print(f'estimated parameters for negative binomial: theta1 = {theta1_hat}, theta2 = {theta2_hat}')

    plot_histogram(data_gamma, 'gamma data')
    theta1_range = np.linspace(0.1, 10, 100)
    theta2_range = np.linspace(0.1, 5, 100)
    plot_log_likelihood(data_gamma, log_likelihood_gamma, theta1_range, theta2_range, 'gamma')

    theta1_hat, theta2_hat = find_max_likelihood(data_gamma, log_likelihood_gamma, theta1_range, theta2_range)
    log_likelihood_hat = log_likelihood_gamma(data_gamma, theta1_hat, theta2_hat)
    print(f'estimated parameters for gamma: theta1 = {theta1_hat}, theta2 = {theta2_hat}')

if __name__ == "__main__":
    main()