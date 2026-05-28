import numpy as np
import matplotlib.pyplot as plt

files = [
    'sample_Bernoulli_1.npy',
    'sample_Bernoulli_2.npy',
    'sample_Exp.npy',
    'sample_Poisson.npy'
]

for file in files:
    data = np.load(file)

    plt.figure()
    plt.hist(data, bins=100, edgecolor='black')

    plt.title(f'Histogram of {file}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    plt.show()