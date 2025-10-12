import numpy as np
import matplotlib.pyplot as plt
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#----------------------------------------
# Given problem data
#----------------------------------------
lam = 1.0  # perpendicular case

A1 = np.array([5, 2, 1])          # Point on Line 1
m1 = np.array([5*lam + 2, -5, 1])  # Direction vector of Line 1

A2 = np.array([0, -0.5, 1])       # Point on Line 2
m2 = np.array([1, 2*lam, 3])      # Direction vector of Line 2

print(f"λ = {lam}")
print(f"m1 = {m1}")
print(f"m2 = {m2}")

#----------------------------------------
# Step 1: Check perpendicularity
#----------------------------------------
dot = np.dot(m1, m2)
print(f"Dot product (m1·m2) = {dot}")
if np.isclose(dot, 0):
    print("✅ Lines are perpendicular")
else:
    print("❌ Lines are not perpendicular")

#----------------------------------------
# Step 2: Check intersection (pure NumPy)
#----------------------------------------
# Solve A1 + k1*m1 = A2 + k2*m2
M = np.column_stack((m1, -m2))
b = A2 - A1

rank_M = np.linalg.matrix_rank(M)
rank_aug = np.linalg.matrix_rank(np.column_stack((M, b)))

if rank_M == rank_aug == 2:
    print("✅ Lines intersect")
    k1, k2 = np.linalg.lstsq(M, b, rcond=None)[0]
    inter_pt = A1 + k1*m1
    print(f"Intersection point: {np.round(inter_pt, 3)}")
else:
    print("❌ Lines do not intersect (skew lines)")
    inter_pt = None

#----------------------------------------
# Step 3: Shortest segment between skew lines (if no intersection)
#----------------------------------------
if inter_pt is None:
    # vector between points on lines
    w0 = A1 - A2
    a = np.dot(m1, m1)
    b_ = np.dot(m1, m2)
    c = np.dot(m2, m2)
    d = np.dot(m1, w0)
    e = np.dot(m2, w0)
    
    denom = a*c - b_**2
    s_c = (b_*d - a*e)/denom
    t_c = (b_*s_c + d)/a
    
    pt_line1 = A1 + t_c*m1
    pt_line2 = A2 + s_c*m2
    inter_segment = np.column_stack((pt_line1, pt_line2))
    print(f"Closest points on lines: {pt_line1}, {pt_line2}")

#----------------------------------------
# Step 4: 3D Visualization
#----------------------------------------
t_vals = np.linspace(-2, 2, 100)
s_vals = np.linspace(-2, 2, 100)

x1, y1, z1 = A1[0] + m1[0]*t_vals, A1[1] + m1[1]*t_vals, A1[2] + m1[2]*t_vals
x2, y2, z2 = A2[0] + m2[0]*s_vals, A2[1] + m2[1]*s_vals, A2[2] + m2[2]*s_vals

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot lines
ax.plot(x1, y1, z1, color='blue', label='Line 1', linewidth=2)
ax.plot(x2, y2, z2, color='red', label='Line 2', linewidth=2)

# Plot intersection point if exists
if inter_pt is not None:
    ax.scatter(*inter_pt, color='green', s=80, label='Intersection')
    ax.text(inter_pt[0], inter_pt[1], inter_pt[2],
            f"({inter_pt[0]:.2f}, {inter_pt[1]:.2f}, {inter_pt[2]:.2f})",
            color='green', fontsize=12, ha='center', va='bottom')

# Plot shortest segment if lines are skew
if inter_pt is None:
    ax.plot(inter_segment[0], inter_segment[1], inter_segment[2], color='purple', 
            linewidth=3, label='Shortest Segment')
    ax.scatter(*pt_line1, color='purple', s=50)
    ax.scatter(*pt_line2, color='purple', s=50)

# Labels and legend
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Plot of Two Lines with Perpendicularity Check")
ax.legend()
ax.grid(True)
ax.view_init(elev=20, azim=45)
plt.tight_layout()
plt.show()

