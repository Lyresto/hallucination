
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import numpy as np
from scipy.optimize import fsolve



def eqn(x, a, b):
    return x + 2*a - b**2

xdata, bdata = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def solve_for_a(x, b):
    


def eqn(a):
    return x + 2*a - b**2

a_guess = 0.5
solution = fsolve(eqn, a_guess)
return solution

result = [solve_for_a(x, b) for x, b in zip(xdata, bdata)]



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
