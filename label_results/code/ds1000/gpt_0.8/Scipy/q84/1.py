import numpy as np
from scipy import integrate

def solve_integral(c_values):
    solutions = []
    for c in c_values:
        result, _ = integrate.quad(lambda x: 2*c*x, 0, 1)
        solutions.append(result)
    return solutions

c_values = np.loadtxt('cooltemp.dat', unpack=True, usecols=[1])
integral_solutions = solve_integral(c_values)
print(integral_solutions)