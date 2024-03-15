
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import scipy.integrate
c, low, high = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
def f(c=5, low=0, high=1):
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

result = f(c, low, high)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
