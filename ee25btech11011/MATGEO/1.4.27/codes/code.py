import numpy as np
import matplotlib.pyplot as plt

# ---- Define Points ----
A = np.array([1, 2], dtype=float)   # Point A (ax, ay)
B = np.array([5, 6], dtype=float)   # Point B (bx, by)

k = 3   # ratio k:1 (external division)

# ---- Section Formula for External Division ----
# C = (k*B - A) / (k - 1)
C = (k * B - A) / (k - 1)

print(f"Position vector of C is: ({C[0]:.2f}, {C[1]:.2f})")

