import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import numpy as np
import pandas as pd
import torch

lens = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def get_mask(lens):
### BEGIN SOLUTION
    mask = []
    max_len = max(lens)
    for length in lens:
        mask.append([1] * length + [0] * (max_len - length))
    mask = torch.LongTensor(mask)
    ### END SOLUTION


### END SOLUTION
mask = get_mask(lens)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(mask, f)
