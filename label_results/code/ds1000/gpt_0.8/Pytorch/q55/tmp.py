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
for i in range(31):
    start = i
    end = i + chunk_dim
    tensor = a[:, :, :, start:end, :]
    tensors_31.append(tensor)



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(tensors_31, f)
