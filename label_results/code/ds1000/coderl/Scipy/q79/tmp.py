
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import scipy.integrate
import numpy as np

N0, time_span = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
from scipy.integrate import solve_ivp
from numpy import array
from itertools import zip_longest




def dN1_dt_simple(t, N1):
    return -100 * N1




def solve_ivp(fun, t_span, y0):
    # Set up initial conditions
    x0 = array([N0,])
    # Run the integrator
    sol = solve_ivp(fun, t_span, x0)
    # Convert solution to array
    return_array = []
    for x, y in zip_longest(x0, sol.y):
        return_array.append(y + x)
    # Return results
    return return_array



result = sol.y
#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
