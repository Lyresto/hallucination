
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

from scipy import sparse
import numpy as np
sA, sB = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def f(sA, sB):



def f(sA = example_sA, sB = example_sB):
    # return the solution in this function
    # result = f(sA, sB)
    # sp.sparse.csr_matrix(np.array([[1,2,3],[4,5,6],[7,8,9]])) * sp.sparse.csr_matrix(np.array([0,1,2]))
    return np.array([[1,2,3],[4,5,6],[7,8,9]]) * sA + np.array([0,1,2]) * sB




result = f(sA, sB)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
