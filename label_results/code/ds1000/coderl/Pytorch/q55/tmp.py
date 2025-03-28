import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import numpy as np
import pandas as pd
import torch

a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
chunk_dim=10
### BEGIN SOLUTION
from itertools import groupby



def tensors_31(a):
    chunk_dim = 10
    tensors = []
    for group in groupby(a, key=len):
        values = [list(j) for j in group]
        split = tuple(zip(*values))
        tensors.append(split)
    return tensors



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(tensors_31, f)
