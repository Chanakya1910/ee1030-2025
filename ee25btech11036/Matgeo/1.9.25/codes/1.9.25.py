import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Parameters
a, b = 5, 2
A = np.array([a+b, b-a])
B = np.array([a-b, a+b])

# Example point P satisfying bx = ay
P = np.array([2.0, (b/a)*2.0])  # pick x=2, y=(b/a)x

# Line bx = ay -> y = (b/a)x
x_vals = np.linspace(-15, 15, 400)
y_vals = (b/a) * x_vals

# Plot line (locus)
plt.plot(x_vals, y_vals, 'r-', label=r'Locus: $bx = ay$')

# Plot points
plt.scatter(*A, color='blue')
plt.scatter(*B, color='green')
plt.scatter(*P, color='purple')

# Annotate points
plt.text(A[0]+0.5, A[1], 'A', fontsize=12, color='blue')
plt.text(B[0]+0.5, B[1], 'B', fontsize=12, color='green')
plt.text(P[0]+0.5, P[1], 'P', fontsize=12, color='purple')

# Circles showing equidistance
d_PA = np.linalg.norm(P - A)
circleA = plt.Circle(A, d_PA, color='blue', fill=False, linestyle='--', alpha=0.5)
circleB = plt.Circle(B, d_PA, color='green', fill=False, linestyle='--', alpha=0.5)
plt.gca().add_patch(circleA)
plt.gca().add_patch(circleB)

# Axes
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Locus of P such that PA = PB")
plt.legend()
plt.axis("equal")
plt.grid(True)
plt.show()
