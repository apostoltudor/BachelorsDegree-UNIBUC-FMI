import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = np.load('sample_normal.npy')

plt.figure()
plt.hist(data, bins=30, alpha=0.7, color='blue')
plt.title('histogram of data')
plt.xlabel('vslue')
plt.ylabel('frequency')
plt.show()

theta1_range = np.linspace(-1, 1, 100)
theta2_range = np.linspace(0.01, 0.1, 100) 
theta1, theta2 = np.meshgrid(theta1_range, theta2_range)

n = len(data)
log_likelihood = np.zeros_like(theta1)

for i in range(theta1.shape[0]):
    for j in range(theta1.shape[1]):
        t1 = theta1[i, j]
        t2 = theta2[i, j]
        log_likelihood[i, j] = -n * np.log(np.sqrt(2 * np.pi * t2)) - (1 / (2 * t2)) * np.sum((data - t1) ** 2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(theta1, theta2, log_likelihood, cmap='viridis')
ax.set_title('log-likelihood function')
ax.set_xlabel('theta1')
ax.set_ylabel('theta2')
ax.set_zlabel('log L')
plt.show()

theta1_hat = np.mean(data)
theta2_hat = np.mean((data - theta1_hat) ** 2)

log_likelihood_hat = -n * np.log(np.sqrt(2 * np.pi * theta2_hat)) - (1 / (2 * theta2_hat)) * np.sum((data - theta1_hat) ** 2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(theta1, theta2, log_likelihood, cmap='viridis', alpha=0.7)
ax.scatter(theta1_hat, theta2_hat, log_likelihood_hat, color='red', s=50)
ax.set_title('log-likelihood function with estimated point')
ax.set_xlabel('theta1')
ax.set_ylabel('theta2')
ax.set_zlabel('log L')
plt.show()
