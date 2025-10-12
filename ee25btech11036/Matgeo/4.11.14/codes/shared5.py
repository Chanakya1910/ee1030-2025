# call_rref.py
import ctypes
import numpy as np
import os

# Load the shared object (adjust path if necessary)
libpath = os.path.abspath("librref.so")
r = ctypes.CDLL(libpath)

# define argument / result types
# void compute_ranks(const double aug[9], double rref_aug[9], double rref_M[9], int *rankAug, int *rankM)
r.compute_ranks.argtypes = [
    ctypes.POINTER(ctypes.c_double),  # aug (input)
    ctypes.POINTER(ctypes.c_double),  # rref_aug (output)
    ctypes.POINTER(ctypes.c_double),  # rref_M (output)
    ctypes.POINTER(ctypes.c_int),     # rankAug (output)
    ctypes.POINTER(ctypes.c_int)      # rankM (output)
]
r.compute_ranks.restype = None

def compute_ranks_python(aug_matrix):
    """
    aug_matrix: numpy array shape (3,3), dtype=float64
    returns: rref_aug (3x3), rref_M (3x3), rankAug (int), rankM (int)
    """
    assert aug_matrix.shape == (3,3)
    aug = np.ascontiguousarray(aug_matrix, dtype=np.float64)
    rref_aug = np.zeros((3,3), dtype=np.float64)
    rref_M = np.zeros((3,3), dtype=np.float64)
    rankAug = np.zeros(1, dtype=np.int32)
    rankM = np.zeros(1, dtype=np.int32)

    # convert to ctypes pointers
    aug_ptr = aug.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    rref_aug_ptr = rref_aug.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    rref_M_ptr = rref_M.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    rankAug_ptr = rankAug.ctypes.data_as(ctypes.POINTER(ctypes.c_int))
    rankM_ptr = rankM.ctypes.data_as(ctypes.POINTER(ctypes.c_int))

    # call C function
    r.compute_ranks(aug_ptr, rref_aug_ptr, rref_M_ptr, rankAug_ptr, rankM_ptr)

    return rref_aug, rref_M, int(rankAug[0]), int(rankM[0])

if __name__ == "__main__":
    # Example: use the augmented matrix from the lambda=1 perpendicular case
    # Columns: m1 (7,-5,1), m2 (1,2,3), augmented (B-A) (-5, -5/2, 0)
    aug = np.array([
        [7.0, 1.0, -5.0],
        [-5.0, 2.0, -2.5],
        [1.0, 3.0, 0.0]
    ], dtype=np.float64)

    rref_aug, rref_M, rankAug, rankM = compute_ranks_python(aug)

    np.set_printoptions(precision=10, suppress=True)
    print("Augmented matrix (input):\n", aug)
    print("\nRREF (augmented):\n", rref_aug.reshape(3,3))
    print("\nRREF (M padded third col zero):\n", rref_M.reshape(3,3))
    print("\nrank(augmented) =", rankAug)
    print("rank(M)         =", rankM)

    if rankAug == rankM:
        print("\nConclusion: system is consistent -> lines intersect.")
    else:
        print("\nConclusion: system is inconsistent -> lines do not intersect (skew).")

