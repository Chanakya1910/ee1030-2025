#include <stdio.h>

// Function to check if bx = ay
// Returns 1 if true, 0 otherwise
int check_equation(double a, double b, double x, double y) {
    double lhs = b * x;
    double rhs = a * y;
    if ( (lhs - rhs) < 1e-6 && (rhs - lhs) < 1e-6 ) {
        return 1;  // condition satisfied
    }
    return 0;  // not satisfied
}
