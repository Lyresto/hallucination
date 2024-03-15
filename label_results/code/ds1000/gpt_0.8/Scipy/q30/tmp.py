
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import numpy as np
from scipy.sparse import lil_matrix
from scipy import sparse

M = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
from scipy.sparse import lil_matrix




def make_symmetric(matrix):
    num_rows, num_cols = matrix.shape
    for i in range(num_rows):
        for j in matrix.rows[i]:
            if j != i:
                matrix[j, i] = matrix[i, j]
    return matrix

# Example usage
M = lil_matrix((10, 10))
# Populate M with some non-zero values

M = make_symmetric(M)



#print(M)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(M, f)
