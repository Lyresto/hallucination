
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
def eqn(x, a, b):
    return x + 2*a - b**2

xdata = np.arange(4)+3
bdata = np.random.randint(0, 10, (4,))
result =... # put solution in this variable
END SOLUTION

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args = (a,b))

fsolve(eqn, x0=0.5, args =
#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
