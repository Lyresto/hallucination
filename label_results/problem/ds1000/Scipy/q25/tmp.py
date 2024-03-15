
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

from scipy import sparse
import numpy as np
a, b = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
# One workaround is to create a new csr_matrix with the diagonal elements removed
# We can do this by creating a new array with the diagonal elements set to 0
# and then using the dia_matrix constructor to create a diagonal matrix
# Finally, we can subtract this diagonal matrix from the original matrix

diagonal = sparse.dia_matrix((np.zeros(2), [0]), shape=(2, 2))
b = b - diagonal

#print(b)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(b, f)
