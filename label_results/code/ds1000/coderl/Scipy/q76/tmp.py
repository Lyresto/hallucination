
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import scipy.optimize
import numpy as np
a, x_true, y, x0, x_lower_bounds = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import scipy.optimize as sp
a = np.array([[0, 0, 1, 1, 1],
             [1, 0, 1, 0, 1],
             [0, 1, 0, 1, 0]])
x_opt = sp.optimize.fmin_l_bfgs_b(lambda x, a: np.dot(a, x ** 2), a, x0=0)
print(x_opt)



#print(out)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(out, f)
