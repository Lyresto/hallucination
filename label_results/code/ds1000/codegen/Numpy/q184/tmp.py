import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
from scipy import interpolate as intp
a, x_new, y_new = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
x_new = np.linspace(0, 2, 4)
y_new = np.linspace(0, 2, 4)
result = intp.interp2d(x_new, y_new, a, kind='linear')

#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
