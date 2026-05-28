import numpy as np
import matplotlib.pyplot as plt

def densitate_normala(x, miu, sigma):
    return (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-((x - miu) ** 2) / (2 * sigma ** 2))

def genereaza_si_afiseaza(n, miu, sigma, alpha, beta):
    X = np.random.normal(miu, sigma, n)
    
    Y_a = alpha + X
    Y_b = beta * X
    Y_c = alpha + beta * X
    
    x_vals = np.linspace(min(Y_a.min(), Y_b.min(), Y_c.min()), max(Y_a.max(), Y_b.max(), Y_c.max()), 1000)
    
    densitate_a = densitate_normala(x_vals, alpha + miu, sigma)
    densitate_b = densitate_normala(x_vals, beta * miu, abs(beta) * sigma)
    densitate_c = densitate_normala(x_vals, alpha + beta * miu, abs(beta) * sigma)
    
    fig, axs = plt.subplots(3, 1, figsize=(8, 12))
    
    axs[0].hist(Y_a, bins=30, density=True, alpha=0.6, color='blue', label='histograma (a)')
    axs[0].plot(x_vals, densitate_a, color='red', label='densitate teoretica (a)')
    axs[0].set_title('cazul (a): Y = alpha + X')
    axs[0].legend()
    
    axs[1].hist(Y_b, bins=30, density=True, alpha=0.6, color='green', label='histograma (b)')
    axs[1].plot(x_vals, densitate_b, color='red', label='densitate teoretica (b)')
    axs[1].set_title('cazul (b): Y = beta * X')
    axs[1].legend()
    
    axs[2].hist(Y_c, bins=30, density=True, alpha=0.6, color='purple', label='histograma (c)')
    axs[2].plot(x_vals, densitate_c, color='red', label='densitate teoretica (c)')
    axs[2].set_title('cazul (c): Y = alpha + beta * X')
    axs[2].legend()
    
    plt.tight_layout()
    plt.show()

def main():
    miu = 0       
    sigma = 1   
    alpha = 2   
    beta = 3    
    n = 10000   
    
    genereaza_si_afiseaza(n, miu, sigma, alpha, beta)

if __name__ == "__main__":
    main()