
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import numpy as np
from scipy.sparse import lil_matrix
from scipy import sparse

M = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
M = lil_matrix(M)
M.make_symmetric()

#print(M)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(M, f)
