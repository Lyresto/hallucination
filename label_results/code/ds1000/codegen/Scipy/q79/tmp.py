
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import scipy.integrate
import numpy as np

N0, time_span = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))

import scipy.integrate
import numpy as np
N0 = 10
time_span = [-0.1, 0.1]
result = scipy.integrate.solve_ivp(fun=dN1_dt_simple, t_span=time_span, y0=[N0,])

result = sol.y
#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
