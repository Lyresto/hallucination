
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
import numpy as np
from scipy.optimize import fsolve
eqn = lambda x, a, b: x + 2 * a - b**2
x0 = 0.5
root_list = fsolve(eqn, x0=x0, args=tuple([a,b]))



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
