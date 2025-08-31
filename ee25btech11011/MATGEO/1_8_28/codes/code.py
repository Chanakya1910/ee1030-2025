
import math

# Define points A and B
A = (3, 4, -5)
B = (-2, 1, 4)

# Midpoint M = (A+B)/2
M = tuple((a + b) / 2 for a, b in zip(A, B))

# Vector AB = B - A
AB = tuple(b - a for a, b in zip(B, A))

# |AB|^2
AB_sq = sum(x**2 for x in AB)

# |A-M|^2 = |AB|^2 / 4
AM_sq = AB_sq / 4

# Input k
k = float(input("Enter value of k: "))

# Radius^2
radius_sq = k*k - AM_sq

print("\n--- Solution for locus of P ---")
print(f"A = {A},  B = {B}")
print(f"Midpoint M = {M}")
print(f"|AB|^2 = {AB_sq}")
print(f"|A-M|^2 = {AM_sq:.2f}")

if radius_sq < 0:
    print("\nNo real sphere exists because radius^2 < 0.")
else:
    print("\nEquation of sphere:")
    print(f"(x - {M[0]})^2 + (y - {M[1]})^2 + (z - {M[2]})^2 = {radius_sq}")
    print(f"Centre: {M}")
    print(f"Radius: {math.sqrt(radius_sq):.4f}")