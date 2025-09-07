import ctypes
import math
import os

# Load the compiled C shared library
if os.name == "nt":
    lib = ctypes.CDLL("./plane.dll")   # Windows
else:
    lib = ctypes.CDLL("./plane.so")    # Linux/macOS

# Function signatures
lib.dot.argtypes = [ctypes.POINTER(ctypes.c_double),
                    ctypes.POINTER(ctypes.c_double),
                    ctypes.c_int]
lib.dot.restype = ctypes.c_double

lib.compute_direction.argtypes = [ctypes.c_double,
                                  ctypes.c_double,
                                  ctypes.POINTER(ctypes.c_double)]
lib.compute_direction.restype = ctypes.c_double


def main():
    alpha = 30.0
    beta  = 120.0

    # allocate space for d[3]
    d = (ctypes.c_double * 3)()

    # Call C function
    lib.compute_direction(alpha, beta, d)

    # Convert to Python list
    d_vec = [d[i] for i in range(3)]
    print(f"Direction vector d = [{d_vec[0]:.4f}, {d_vec[1]:.4f}, {d_vec[2]:.4f}]")

    # Verify with C dot()
    arr = (ctypes.c_double * 3)(*d_vec)
    check = lib.dot(arr, arr, 3)
    print(f"d^T d = {check:.4f} (should be 1)")

    # Angle with Z-axis
    gamma_deg = math.degrees(math.acos(d_vec[2]))
    print(f"Angle with positive Z-axis = {gamma_deg:.2f} degrees")


if __name__ == "__main__":
    main()
