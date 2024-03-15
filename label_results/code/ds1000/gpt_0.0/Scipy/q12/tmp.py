
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

from scipy import sparse
import numpy as np
sA, sB = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
def f(sA, sB):
    result = sA.multiply(sparse.csr_matrix(sB).transpose())
        ### END SOLUTION
    return result
    

result = f(sA, sB)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
