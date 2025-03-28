
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import numpy as np
from scipy.sparse import csr_matrix

M, row, column = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
row = [2, 1]
column = [3, 0]
result = M.getrow(row)

#print(result)



with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
