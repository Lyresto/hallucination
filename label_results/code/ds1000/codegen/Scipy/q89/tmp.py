
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
from scipy import sparse
import numpy as np
import math
sa = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
sa =... # put solution in this variable
sa = np.dot(sa, np.random.rand(10, 10))

#print(sa)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(sa, f)
