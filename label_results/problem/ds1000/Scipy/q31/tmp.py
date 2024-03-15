
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import numpy as np
from scipy.sparse import lil_matrix
def f(sA):
    # convert to csr format for efficient row slicing
    sA = sA.tocsr()
    # create a new lil matrix for the symmetric version
    sA_sym = lil_matrix(sA.shape, dtype=sA.dtype)
    # iterate over rows of sA
    for i in range(sA.shape[0]):
        # get the indices and values of non-zero elements in the i-th row
        row_indices, row_values = sA[i].indices, sA[i].data
        # iterate over the non-zero elements in the i-th row
        for j, val in zip(row_indices, row_values):
            # set the corresponding element in the symmetric matrix
            sA_sym[i, j] = val
            sA_sym[j, i] = val
    # return the symmetric matrix in csr format
    return sA_sym.tocsr()
    ### END SOLUTION
sA = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))

result = f(sA)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
