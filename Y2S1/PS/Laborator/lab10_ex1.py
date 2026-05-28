import numpy as np
import matplotlib.pyplot as plt


def simulate_and_plot(case, N=1000):
    X = np.random.uniform(-1, 1, N)

    if case == 'i':
        Y = np.random.uniform(-1, 1, N)
    elif case == 'ii':
        Y = X ** 2
    elif case == 'iii':
        Y = X ** 3 + X
    elif case == 'iv':
        Y = X
    elif case == 'v':
        Y = -X
    else:
        raise ValueError("caz invalid")

    plt.figure(figsize=(8, 6))
    plt.scatter(X, Y, alpha=0.5, edgecolor='k')
    plt.title(f'simulari pentru cazul {case}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

    covariance = np.cov(X, Y)[0, 1]
    correlation = np.corrcoef(X, Y)[0, 1]

    print(f'case {case}:')
    print(f'covariance: {covariance}')
    print(f'correlation: {correlation}\n')


def main():
    cases = ['i', 'ii', 'iii', 'iv', 'v']
    for case in cases:
        simulate_and_plot(case)


if __name__ == "__main__":
    main()