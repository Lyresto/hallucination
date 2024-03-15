
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import scipy.optimize
import numpy as np
a, x_true, y, x0, x_lower_bounds = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def objective(x):
    return np.sum(a.dot(x ** 2))

out = scipy.optimize.minimize(objective, x0, method='L-BFGS-B', bounds=[(lb, None) for lb in x_lower_bounds])



#print(out)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(out, f)
