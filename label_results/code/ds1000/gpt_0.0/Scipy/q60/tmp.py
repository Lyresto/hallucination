
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import scipy.interpolate
x, array, x_new = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
new_array = scipy.interpolate.interp1d(x, array, axis=0)(x_new)

#print(new_array)



with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(new_array, f)
