import numpy as np
from scipy import integrate

def solve_integral(c_values):
    integrals = []
    for c in c_values:
        # define the integrand function
        integrand = lambda x: 2*c*x
        # integrate using quad function
        result, error = integrate.quad(integrand, 0, 1)
        integrals.append(result)
    return np.array(integrals)

# example usage
c_values = np.array([1, 2, 3, 4, 5])
solutions = solve_integral(c_values)
print(solutions)