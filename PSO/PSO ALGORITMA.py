import numpy as np

def f(x):
    # Define your fitness function here
    return x**2  # Example: a simple quadratic function

# Initialize parameters
num_particles = 10
num_dimensions = 1  # Assuming a single dimension for simplicity
x = np.random.uniform(-10, 10, (num_particles, num_dimensions))  # Initial positions
v = np.random.uniform(-1, 1, (num_particles, num_dimensions))  # Initial velocities
p_best = x.copy()  # Initial pBest is the initial position
g_best = x[np.argmin([f(xi) for xi in x])]  # Global best position
c1, c2 = 2.0, 2.0  # Cognitive and social coefficients
w = 0.5  # Inertia weight
max_iterations = 100

for iteration in range(max_iterations):
    # Evaluate fitness
    fitness = np.array([f(xi) for xi in x])

    # Update pBest
    for i in range(num_particles):
        if f(x[i]) < f(p_best[i]):
            p_best[i] = x[i]

    # Update gBest
    g_best = p_best[np.argmin([f(p) for p in p_best])]

    # Update velocities and positions
    r1, r2 = np.random.random((num_particles, num_dimensions)), np.random.random((num_particles, num_dimensions))
    v = w * v + c1 * r1 * (p_best - x) + c2 * r2 * (g_best - x)
    x = x + v
print("Optimal solution (gBest):", g_best)
print("Optimal value (f(gBest)):", f(g_best))
