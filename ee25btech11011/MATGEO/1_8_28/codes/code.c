#include <stdio.h>
#include <math.h>

int main() {
    // Define points A and B
    double A[3] = {3, 4, -5};
    double B[3] = {-2, 1, 4};
    double M[3];   // midpoint

    // Midpoint M = (A+B)/2
    M[0] = (A[0] + B[0]) / 2.0;
    M[1] = (A[1] + B[1]) / 2.0;
    M[2] = (A[2] + B[2]) / 2.0;

    // Vector AB = B - A
    double AB[3];
    AB[0] = B[0] - A[0];
    AB[1] = B[1] - A[1];
    AB[2] = B[2] - A[2];

    // |AB|^2
    double AB_sq = AB[0]*AB[0] + AB[1]*AB[1] + AB[2]*AB[2];

    // |A-M|^2 = |AB|^2 / 4
    double AM_sq = AB_sq / 4.0;

    // Input k
    double k;
    printf("Enter value of k: ");
    scanf("%lf", &k);

    // Radius^2
    double radius_sq = k*k - AM_sq;

    printf("\n--- Solution for locus of P ---\n");
    printf("Midpoint M = (%.2f, %.2f, %.2f)\n", M[0], M[1], M[2]);
    printf("|AB|^2 = %.2f\n", AB_sq);
    printf("|A-M|^2 = %.2f\n", AM_sq);

    if (radius_sq < 0) {
        printf("\nNo real sphere exists because radius^2 < 0.\n");
    } else {
        printf("\nEquation of sphere:\n");
        printf("(x - %.2f)^2 + (y - %.2f)^2 + (z - %.2f)^2 = %.2f\n",
               M[0], M[1], M[2], radius_sq);
        printf("Centre: (%.2f, %.2f, %.2f)\n", M[0], M[1], M[2]);
        printf("Radius: %.4f\n", sqrt(radius_sq));
    }

    return 0;
}