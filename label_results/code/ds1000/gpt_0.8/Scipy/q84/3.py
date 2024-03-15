import scipy.integrate
import numpy as np

def solve_integral(c_values):
    I = []
    for c in c_values:
        result, error = scipy.integrate.quad(lambda x: 2*c*x, 0, 1)
        I.append(result)
    return np.array(I)

# Example usage
c_values = [1, 2, 3, 4, 5]
results = solve_integral(c_values)
print(results)