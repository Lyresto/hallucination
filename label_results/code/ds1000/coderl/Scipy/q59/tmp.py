
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import numpy as np
from scipy.sparse import csr_matrix

M, row, column = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
M = csr_matrix(arr)
r = M.getrow(row)
c = M.getcol(column)



#print(result)



with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
