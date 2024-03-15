import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import numpy as np
import pandas as pd
import torch

A_log, B = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
def solve(A_log, B):
### BEGIN SOLUTION

    C = np.zeros(A_log.shape)
    for i in range(A_log.shape[0]):
        C[i] = A_log[i]
    ### END SOLUTION
    return C

### END SOLUTION
C = solve(A_log, B)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(C, f)
