import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gammaln

files = [
    'sample_Bernoulli_1.npy',
    'sample_Poisson.npy',
    'sample_Geom.npy',
    'sample_Exp.npy'
]


def log_likelihood_bernoulli(data, theta):
    n = len(data)
    return n * np.log(theta) * np.sum(data) + (n - np.sum(data)) * np.log(1 - theta)


def log_likelihood_poisson(data, theta):
    n = len(data)
    return n * np.log(theta) * np.sum(data) - n * theta - np.sum(gammaln(data + 1))


def log_likelihood_geometric(data, theta):
    n = len(data)
    return n * np.log(theta) + (np.sum(data) - n) * np.log(1 - theta)


def log_likelihood_exponential(data, theta):
    n = len(data)
    return -n * np.log(1 / theta) - theta * np.sum(data)


def estimate_theta(data, distribution_type):
    if distribution_type == 'bernoulli':
        return np.mean(data)
    elif distribution_type == 'poisson':
        return np.mean(data)
    elif distribution_type == 'geometric':
        return len(data) / np.sum(data)
    elif distribution_type == 'exponential':
        return 1 / np.mean(data)


for file in files:
    data = np.load(file)

    if 'Bernoulli' in file:
        distribution_type = 'bernoulli'
        theta_range = np.linspace(0.01, 0.99, 100)
    elif 'Poisson' in file:
        distribution_type = 'poisson'
        theta_range = np.linspace(0.01, 50, 100)
    elif 'Geom' in file:
        distribution_type = 'geometric'
        theta_range = np.linspace(0.01, 0.99, 100)
    elif 'Exp' in file:
        distribution_type = 'exponential'
        theta_range = np.linspace(0.01, 50, 100)

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.hist(data, bins=30, alpha=0.7, color='blue')
    plt.title(f'Histogram of {file}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    log_likelihoods = []
    for theta in theta_range:
        if distribution_type == 'bernoulli':
            log_likelihoods.append(log_likelihood_bernoulli(data, theta))
        elif distribution_type == 'poisson':
            log_likelihoods.append(log_likelihood_poisson(data, theta))
        elif distribution_type == 'geometric':
            log_likelihoods.append(log_likelihood_geometric(data, theta))
        elif distribution_type == 'exponential':
            log_likelihoods.append(log_likelihood_exponential(data, theta))

    theta_hat = estimate_theta(data, distribution_type)

    plt.subplot(1, 2, 2)
    plt.plot(theta_range, log_likelihoods, label='Log-Likelihood')
    plt.scatter(theta_hat, log_likelihood_bernoulli(data, theta_hat) if distribution_type == 'bernoulli' else
    log_likelihood_poisson(data, theta_hat) if distribution_type == 'poisson' else
    log_likelihood_geometric(data, theta_hat) if distribution_type == 'geometric' else
    log_likelihood_exponential(data, theta_hat), color='red', label=f'θ_hat = {theta_hat:.2f}')
    plt.title(f'Log-Likelihood of {file}')
    plt.xlabel('Theta')
    plt.ylabel('Log-Likelihood')
    plt.legend()

    plt.tight_layout()
    plt.show()