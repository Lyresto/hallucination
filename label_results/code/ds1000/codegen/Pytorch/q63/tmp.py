import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import numpy as np
import pandas as pd
import torch

a, b = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
def solve(a, b):
### BEGIN SOLUTION

    result = np.zeros((a.shape[0], b.shape[0]))
    for i in range(a.shape[0]):
        for j in range(b.shape[0]):
            result[i, j] = np.mean(a[i, :] + b[j, :])
    ### END SOLUTION
    return result

### END SOLUTION
result = solve(a, b)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
