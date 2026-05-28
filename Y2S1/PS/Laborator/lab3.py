#ex1
import numpy as np

def estimate_probability_uniform(a, b, c, d, num_simulations=100000000):
    random_numbers = np.random.uniform(a, b, num_simulations)
    count_in_interval = np.sum((random_numbers >= c) & (random_numbers <= d))
    estimated_probability = count_in_interval / num_simulations
    return estimated_probability

def main():
    a = 0
    b = 10
    c = 3
    d = 7
    probability = estimate_probability_uniform(a, b, c, d)
    print(f"probabilitatea este: {probability:.4f}")

if __name__ == "__main__":
    main()

#ex2
import numpy as np
import matplotlib.pyplot as plt

def estimate_probability_rectangle(a1, b1, c1, d1, a2, b2, c2, d2, num_simulations=10000):
    x = np.random.uniform(a1, b1, num_simulations)
    y = np.random.uniform(a2, b2, num_simulations)
    count_in_rectangle = np.sum((x >= c1) & (x <= d1) & (y >= c2) & (y <= d2))
    estimated_probability = count_in_rectangle / num_simulations
    return estimated_probability

def plot_rectangle_simulation(a1, b1, c1, d1, a2, b2, c2, d2, num_simulations=10000):
    x = np.random.uniform(a1, b1, num_simulations)
    y = np.random.uniform(a2, b2, num_simulations)
    inside_rectangle = (x >= c1) & (x <= d1) & (y >= c2) & (y <= d2)
    plt.figure(figsize=(8, 8))
    plt.scatter(x[inside_rectangle], y[inside_rectangle], color='green', s=1, label='Inside Rectangle')
    plt.scatter(x[~inside_rectangle], y[~inside_rectangle], color='red', s=1, label='Outside Rectangle')
    plt.axvline(c1, color='blue', linestyle='--')
    plt.axvline(d1, color='blue', linestyle='--')
    plt.axhline(c2, color='blue', linestyle='--')
    plt.axhline(d2, color='blue', linestyle='--')
    plt.title(f'simularea probabilității in dreptunghi [{c1}, {d1}] x [{c2}, {d2}]')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    a1, b1, c1, d1 = 0, 10, 2, 8
    a2, b2, c2, d2 = 0, 10, 3, 7
    probability = estimate_probability_rectangle(a1, b1, c1, d1, a2, b2, c2, d2)
    print(f"probabilitatea ca (x, y) ss fie in [{c1}, {d1}] x [{c2}, {d2}] este: {probability:.4f}")
    plot_rectangle_simulation(a1, b1, c1, d1, a2, b2, c2, d2)

if __name__ == "__main__":
    main()

#ex 3
import numpy as np
import matplotlib.pyplot as plt

def estimate_area_of_circle(r, num_simulations=10000):
    x = np.random.uniform(-r, r, num_simulations)
    y = np.random.uniform(-r, r, num_simulations)
    inside_circle = np.sum(x**2 + y**2 <= r**2)
    estimated_area = (inside_circle / num_simulations) * (4 * r**2)
    return estimated_area

def estimate_volume_of_sphere(r, d, num_simulations=100000):
    points = np.random.uniform(-r, r, (num_simulations, d))
    inside_sphere = np.sum(np.linalg.norm(points, axis=1) <= r)
    estimated_volume = (inside_sphere / num_simulations) * (2 * r)**d
    return estimated_volume

def plot_circle_simulation(r, num_simulations=10000):
    x = np.random.uniform(-r, r, num_simulations)
    y = np.random.uniform(-r, r, num_simulations)
    inside_circle = (x**2 + y**2) <= r**2
    plt.figure(figsize=(6, 6))
    plt.scatter(x[inside_circle], y[inside_circle], color='green', s=1, label='Inside Circle')
    plt.scatter(x[~inside_circle], y[~inside_circle], color='red', s=1, label='Outside Circle')
    circle = plt.Circle((0, 0), r, color='blue', fill=False, linestyle='--', label='Circle Boundary')
    plt.gca().add_artist(circle)
    plt.gca().set_aspect('equal')
    plt.title(f'simularea ariei discului de raza {r}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

def main():
    r = 1
    estimated_area = estimate_area_of_circle(r)
    print(f"aria estimata a discului de raza {r} este: {estimated_area:.4f}")
    for d in [1, 10]:
        estimated_volume = estimate_volume_of_sphere(r, d)
        print(f"volumul sferei de raza {r} cu dimensiunea {d} este: {estimated_volume:.4f}")
    plot_circle_simulation(r)

if __name__ == "__main__":
    main()

#ex 4
import numpy as np
import matplotlib.pyplot as plt

def estimate_area_of_ellipse(a, b, num_simulations=10000):
    x = np.random.uniform(-a, a, num_simulations)
    y = np.random.uniform(-b, b, num_simulations)
    inside_ellipse = np.sum((x**2 / a**2) + (y**2 / b**2) <= 1)
    estimated_area = (inside_ellipse / num_simulations) * (4 * a * b)
    return estimated_area

def plot_ellipse_simulation(a, b, num_simulations=10000):
    x = np.random.uniform(-a, a, num_simulations)
    y = np.random.uniform(-b, b, num_simulations)
    inside_ellipse = (x**2 / a**2) + (y**2 / b**2) <= 1
    plt.figure(figsize=(8, 8))
    plt.scatter(x[inside_ellipse], y[inside_ellipse], color='green', s=1, label='Inside Ellipse')
    plt.scatter(x[~inside_ellipse], y[~inside_ellipse], color='red', s=1, label='Outside Ellipse')
    ellipse = plt.Rectangle((-a, -b), 2*a, 2*b, color='blue', fill=False, linestyle='--', label='Bounding Box')
    plt.gca().add_artist(ellipse)
    plt.gca().set_aspect('equal')
    plt.title(f'aimularea ariei elipsei avand semiaxele a={a}, b={b}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    a, b = 3, 2
    estimated_area = estimate_area_of_ellipse(a, b)
    print(f"aria elipsei cu semiaxele a={a} si b={b}: {estimated_area:.4f}")
    plot_ellipse_simulation(a, b)

if __name__ == "__main__":
    main()

#ex 5
import numpy as np
import matplotlib.pyplot as plt

def estimate_intersection_area(P, r, a, b, num_simulations=10000):
    x = np.random.uniform(-a, a, num_simulations)
    y = np.random.uniform(-b, b, num_simulations)
    inside_circle = (x - P[0])**2 + (y - P[1])**2 <= r**2
    inside_ellipse = (x**2 / a**2) + (y**2 / b**2) <= 1
    intersection_points = np.sum(inside_circle & inside_ellipse)
    bounding_area = 4 * a * b
    estimated_intersection_area = (intersection_points / num_simulations) * bounding_area
    return estimated_intersection_area

def plot_intersection_simulation(P, r, a, b, num_simulations=10000):
    x = np.random.uniform(-a, a, num_simulations)
    y = np.random.uniform(-b, b, num_simulations)
    inside_circle = (x - P[0])**2 + (y - P[1])**2 <= r**2
    inside_ellipse = (x**2 / a**2) + (y**2 / b**2) <= 1
    intersection = inside_circle & inside_ellipse
    plt.figure(figsize=(8, 8))
    plt.scatter(x[intersection], y[intersection], color='green', s=1, label='In Intersection')
    plt.scatter(x[~intersection], y[~intersection], color='red', s=1, label='Outside Intersection')
    circle = plt.Circle(P, r, color='blue', fill=False, linestyle='--', label='Discul B(P, r)')
    ellipse = plt.Rectangle((-a, -b), 2 * a, 2 * b, color='purple', fill=False, linestyle='--', label='Bounding Box')
    plt.gca().add_artist(circle)
    plt.gca().add_artist(ellipse)
    plt.gca().set_aspect('equal')
    plt.title(f'simularea intersectiei dintre discul B({P}, {r}) si elipsa E(0, {a}, {b})')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    P = (2, 2)
    r = np.sqrt(2)
    a, b = 3, 2
    estimated_area = estimate_intersection_area(P, r, a, b)
    print(f"aria intersectiei dintre discul B({P}, {r:.2f}) si elipsa E(0, {a}, {b}) este: {estimated_area:.4f}")
    plot_intersection_simulation(P, r, a, b)

if __name__ == "__main__":
    main()
