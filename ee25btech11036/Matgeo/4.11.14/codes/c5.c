// rref.c
#include <stdio.h>
#include <math.h>
#include <string.h>

static const double EPS = 1e-12;

/* perform Gauss-Jordan on 3x3 matrix src, write result to dst (row-major).
   Returns rank (number of non-zero rows in RREF). */
static int gauss_jordan_3x3(const double src[9], double dst[9]) {
    double A[3][3];
    for (int r = 0; r < 3; ++r)
        for (int c = 0; c < 3; ++c)
            A[r][c] = src[r*3 + c];

    int row = 0;
    for (int col = 0; col < 3 && row < 3; ++col) {
        /* find pivot: row >= row with max abs in column col */
        int sel = row;
        double maxv = fabs(A[sel][col]);
        for (int i = row+1; i < 3; ++i) {
            double v = fabs(A[i][col]);
            if (v > maxv) { maxv = v; sel = i; }
        }
        if (maxv < EPS) continue; /* no pivot in this column */

        /* swap selected row with current row */
        if (sel != row) {
            for (int j = 0; j < 3; ++j) {
                double tmp = A[row][j]; A[row][j] = A[sel][j]; A[sel][j] = tmp;
            }
        }

        /* normalize pivot row */
        double pivot = A[row][col];
        for (int j = 0; j < 3; ++j) A[row][j] /= pivot;

        /* eliminate other rows */
        for (int i = 0; i < 3; ++i) {
            if (i == row) continue;
            double factor = A[i][col];
            if (fabs(factor) < EPS) continue;
            for (int j = 0; j < 3; ++j) {
                A[i][j] -= factor * A[row][j];
            }
        }

        row++;
    }

    /* copy back to dst */
    for (int r = 0; r < 3; ++r)
        for (int c = 0; c < 3; ++c)
            dst[r*3 + c] = A[r][c];

    /* count non-zero rows (as rank) */
    int rank = 0;
    for (int r = 0; r < 3; ++r) {
        int nonzero = 0;
        for (int c = 0; c < 3; ++c) {
            if (fabs(A[r][c]) > EPS) { nonzero = 1; break; }
        }
        if (nonzero) rank++;
    }
    return rank;
}

/* Public symbol for ctypes */
void compute_ranks(const double aug[9],
                   double rref_aug[9],
                   double rref_M[9],
                   int *rankAug,
                   int *rankM)
{
    /* compute RREF of augmented matrix */
    *rankAug = gauss_jordan_3x3(aug, rref_aug);

    /* build matrix M (first two columns of aug), pad third column with zeros */
    double Mpad[9];
    for (int r = 0; r < 3; ++r) {
        Mpad[r*3 + 0] = aug[r*3 + 0]; /* col 0 */
        Mpad[r*3 + 1] = aug[r*3 + 1]; /* col 1 */
        Mpad[r*3 + 2] = 0.0;         /* zero augmented column */
    }

    *rankM = gauss_jordan_3x3(Mpad, rref_M);
}

