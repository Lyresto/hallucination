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
    C = B[:, A_log.nonzero().squeeze()]
    return C
    ### END SOLUTION
### END SOLUTION
C = solve(A_log, B)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(C, f)
