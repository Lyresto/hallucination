
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import numpy as np
from scipy.sparse import lil_matrix
def f(sA):

    sA = np.random.random((10, 10))
    ### END SOLUTION
    return sA

sA = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))

result = f(sA)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
