#ex 5
import numpy as np
import matplotlib.pyplot as plt

n_simulations = 100000

P = np.array([2, 2])  
r = np.sqrt(2)  
a = 3  
b = 2  
x = np.random.uniform(-4, 4, n_simulations)
y = np.random.uniform(-4, 4, n_simulations)

distances_to_P = np.sqrt((x - P[0])**2 + (y - P[1])**2)

inside_circle = distances_to_P <= r

inside_ellipse = (x**2 / a**2) + (y**2 / b**2) <= 1

inside_both = np.sum(inside_circle & inside_ellipse)

area_intersection = (inside_both / n_simulations) * 16 

print(f"Estimated area of the intersection: {area_intersection}")

plt.figure(figsize=(6, 6))
plt.scatter(x[inside_both], y[inside_both], s=1, c='blue', label='Inside both')
plt.scatter(x[inside_circle & ~inside_ellipse], y[inside_circle & ~inside_ellipse], s=1, c='red', label='Inside circle only')
plt.scatter(x[~inside_circle & inside_ellipse], y[~inside_circle & inside_ellipse], s=1, c='green', label='Inside ellipse only')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Intersection of Circle and Ellipse')
plt.legend()
plt.xlim([-4, 4])
plt.ylim([-4, 4])
plt.grid(True)
plt.show()

#ex 6
import numpy as np
import matplotlib.pyplot as plt

def f1(x, y):
    return x**2 + y**4 + 2*x*y - 1

def f2(x, y):
    return y**2 + x**2 * np.cos(x) - 1

def f3(x, y):
    return np.exp(x**2) + y**2 - 4 + 2.99 * np.cos(y)

def monte_carlo_area(f, x_range, y_range, num_points=100000):
    x_random = np.random.uniform(x_range[0], x_range[1], num_points)
    y_random = np.random.uniform(y_range[0], y_range[1], num_points)
    count_inside = np.sum(f(x_random, y_random) <= 0)
    area = (x_range[1] - x_range[0]) * (y_range[1] - y_range[0]) * (count_inside / num_points)
    return area

area_d1 = monte_carlo_area(f1, [-3, 3], [-3, 3])
area_d2 = monte_carlo_area(f2, [-5, 5], [-5, 5])
area_d3 = monte_carlo_area(f3, [-2.5, 2.5], [-2.5, 2.5])

print(f"area_d1: {area_d1}")
print(f"area_d2: {area_d2}")
print(f"area_d3: {area_d3}")

def plot_domain(f, x_range, y_range, title):
    x = np.linspace(x_range[0], x_range[1], 400)
    y = np.linspace(y_range[0], y_range[1], 400)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    plt.contourf(X, Y, Z, levels=[-np.inf, 0], colors=['lightblue'])
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plot_domain(f1, [-3, 3], [-3, 3], 'Domain D1')

plt.subplot(1, 3, 2)
plot_domain(f2, [-5, 5], [-5, 5], 'Domain D2')

plt.subplot(1, 3, 3)
plot_domain(f3, [-2.5, 2.5], [-2.5, 2.5], 'Domain D3')

plt.tight_layout()
plt.show()

#ex 7
import numpy as np

r = 1  
R = 2 * r  

def estimate_pi(num_points=1000000):
    x_random = np.random.uniform(-R/2, R/2, num_points)
    y_random = np.random.uniform(-R/2, R/2, num_points)
    count_inside_circle = np.sum(x_random**2 + y_random**2 <= r**2)
    area_circle = (count_inside_circle / num_points) * (R**2)
    pi_estimate = area_circle / (r**2)
    return pi_estimate

pi_estimate = estimate_pi()
print(f"estimated π: {pi_estimate}")

#ex 8
import numpy as np

needle_length = 1.0
line_distance = 2.0


def estimate_pi_buffon(num_needles=1000000):
    count_crosses = 0
    for _ in range(num_needles):
        center = np.random.uniform(0, line_distance / 2)
        angle = np.random.uniform(0, np.pi / 2)

        if center <= (needle_length / 2) * np.sin(angle):
            count_crosses += 1

    pi_estimate = (2 * needle_length * num_needles) / (line_distance * count_crosses)
    return pi_estimate


pi_estimate = estimate_pi_buffon()
print(f"estimated π: {pi_estimate}")
