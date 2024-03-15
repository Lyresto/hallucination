
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import scipy.integrate
import numpy as np

N0, time_span = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
def dN1_dt(t, N1):
    return -100 * N1 + np.cos(t)

sol = scipy.integrate.solve_ivp(fun=dN1_dt, t_span=time_span, y0=[N0,], dense_output=True)

t_eval = np.linspace(time_span[0], time_span[1], 1000)
result = sol.sol(t_eval)

result = sol.y
#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
