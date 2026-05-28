import numpy as np
import matplotlib.pyplot as plt

data = np.load('sample_Normal.npy')

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(data, bins=30, alpha=0.7, color='blue')
plt.title('histogram of sample_Normal.npy')
plt.xlabel('value')
plt.ylabel('frequency')

mu = 0
n = len(data)
theta2_range = np.linspace(0.001, 0.1, 100)
log_likelihoods_theta2 = []

for theta2 in theta2_range:
    log_likelihood = -n * np.log(2 * np.pi * theta2) - (1 / (2 * theta2)) * np.sum((data - mu) ** 2)
    log_likelihoods_theta2.append(log_likelihood)

theta2_hat = np.var(data)
print(f"estimated theta2: {theta2_hat}")

plt.subplot(1, 2, 2)
plt.plot(theta2_range, log_likelihoods_theta2, label='log-likelihood theta2')
plt.scatter(theta2_hat, -n * np.log(2 * np.pi * theta2_hat) - (1 / (2 * theta2_hat)) * np.sum((data - mu) ** 2), color='red', label=f'θ2_hat = {theta2_hat:.4f}')
plt.title('log-likelihood for variance (theta2)')
plt.xlabel('theta2')
plt.ylabel('log-likelihood')
plt.legend()

plt.tight_layout()
plt.show()

sigma2 = 0.01
theta1_range = np.linspace(-1, 1, 100)
log_likelihoods_theta1 = []

for theta1 in theta1_range:
    log_likelihood = -n * np.log(np.sqrt(2 * np.pi * sigma2)) - (1 / (2 * sigma2)) * np.sum((data - theta1) ** 2)
    log_likelihoods_theta1.append(log_likelihood)

theta1_hat = np.mean(data)
print(f"estimated theta1: {theta1_hat}")

plt.figure(figsize=(6, 6))
plt.plot(theta1_range, log_likelihoods_theta1, label='log-likelihood for theta1')
plt.scatter(theta1_hat, -n * np.log(np.sqrt(2 * np.pi * sigma2)) - (1 / (2 * sigma2)) * np.sum((data - theta1_hat) ** 2), color='red', label=f'θ1_hat = {theta1_hat:.4f}')
plt.title('log-likelihood for mean (theta1)')
plt.xlabel('theta1')
plt.ylabel('log-likelihood')
plt.legend()
plt.show()