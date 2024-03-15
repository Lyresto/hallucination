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
tensors_31 = []
for i in range(a.shape[2] - chunk_dim + 1):
    tensors_31.append(a[:, :, i:i+chunk_dim, :, :])



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(tensors_31, f)
