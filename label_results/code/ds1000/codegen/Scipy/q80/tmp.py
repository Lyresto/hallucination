
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
from scipy.optimize import minimize

def function(x):
    return -1*(18*x[0]+16*x[1]+12*x[2]+11*x[3])

I = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
x0=I


cons=[]
steadystate={'type':'eq', 'fun': lambda x: x.sum()-I.sum() }
cons.append(steadystate)

import numpy as np
from scipy.optimize import minimize

def function(x):
    return -1*(18*x[0]+16*x[1]+12*x[2]+11*x[3])

I=np.array((20,50,50,80))
x0=I

cons=[]
steadystate={'type':'eq', 'fun': lambda x: x.sum()-I.sum() }
cons.append(steadystate)

out=minimize(function, x0, method="SLSQP", constraints=cons)
x=out["x"]


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(x, f)
