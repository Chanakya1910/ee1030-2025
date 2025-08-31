
import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Define points A and B
    A = np.array([3, 4, -5], dtype=float)
    B = np.array([-2, 1, 4], dtype=float)

    # Midpoint M = (A+B)/2
    M = (A + B) / 2

    # Vector AB = B - A
    AB = B - A

    # |AB|^2
    AB_sq = np.dot(AB, AB)

    # |A-M|^2 = |AB|^2 / 4
    AM_sq = AB_sq / 4

    # Choose k (must satisfy k^2 >= AM_sq)
    k = math.sqrt(AM_sq + 10)  # arbitrary valid choice
    radius_sq = k*k - AM_sq
    radius = math.sqrt(radius_sq)

    # Print results
    print("Point A:", A)
    print("Point B:", B)
    print("Midpoint M (centre):", M)
    print("||AB||^2 =", AB_sq)
    print("||A-M||^2 =", AM_sq)
    print("Chosen k =", k)
    print("Radius of sphere =", radius)
    print(f"Sphere equation: (x-{M[0]})^2 + (y-{M[1]})^2 + (z-{M[2]})^2 = {radius**2}")

    # --- Plot the sphere ---
    fig = plt.figure(figsize=(7,7))
    ax = fig.add_subplot(111, projection='3d')

    # Sphere surface
    u = np.linspace(0, 2*np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    x = M[0] + radius * np.outer(np.cos(u), np.sin(v))
    y = M[1] + radius * np.outer(np.sin(u), np.sin(v))
    z = M[2] + radius * np.outer(np.ones_like(u), np.cos(v))
    ax.plot_surface(x, y, z, color='skyblue', alpha=0.4, edgecolor='k')

    # Plot A, B, M
    ax.scatter(*A, color='red', s=80, label='A (3,4,-5)')
    ax.scatter(*B, color='green', s=80, label='B (-2,1,4)')
    ax.scatter(*M, color='blue', s=100, marker='^', label='M (centre)')

    # Connect A and B
    ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], 'k--', label='AB')

    # Labels
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('Locus Sphere for P')
    ax.legend()

    plt.show()

if __name__ == "__main__":
    main()