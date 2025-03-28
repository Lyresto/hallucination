
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import scipy.integrate
import numpy as np

N0, time_span = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
from scipy.integrate import solve_ivp
import numpy as np




def dN1_dt(t, N1):
    return -100 * N1 - np.cos(t)

sol = solve_ivp(fun=dN1_dt, t_span=time_span, y0=[N0,])
result = sol.y


result = sol.y
#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
