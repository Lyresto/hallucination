
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
import scipy.sparse as sp




def have_element(i, j):
    return i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    



def make_symmetric():
    lil = sp.lil_matrix(M)
    for i in range(lil.shape[0]):
        for j in range(lil.shape[1]):
            if i!= j:
                lil[i, j] = lil[j, i]
    lil.make_symmetric()
    return lil



#print(M)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(M, f)
