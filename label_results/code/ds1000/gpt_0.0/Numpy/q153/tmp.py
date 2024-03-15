import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
A, B = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
# One way to do it without a for loop is to use np.logical_and and np.isin functions
mask = np.logical_and(A>=B[0], A<=B[-1]) # create a boolean mask for elements in A that are in the range of B
C = A[np.isin(A, B, invert=True) & mask] # use np.isin to exclude elements in B and apply the mask to A

#print(C)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(C, file)
