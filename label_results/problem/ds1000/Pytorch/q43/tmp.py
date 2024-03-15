import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import numpy as np
import pandas as pd
import torch

softmax_output = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
_, y = torch.max(torch.tensor(softmax_output), 1)
y = y.numpy().reshape(-1, 1)

### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(y, f)
