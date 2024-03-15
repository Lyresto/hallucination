import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import numpy as np
import pandas as pd
import torch

a, lengths = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
from itertools import chain




def tenzor_tensor(a, lengths):
    t = [[0] * len(a[0]) for _ in range(len(a))]
    for b, c in zip(a, lengths):
        t[b // len(a[0])][c // len(a[0])] = 1
    return chain.from_iterable(t)



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(a, f)
