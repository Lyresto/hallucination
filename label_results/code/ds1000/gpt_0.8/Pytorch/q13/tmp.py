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
    import torch
    
    C = torch.LongTensor([[1, 3], [4, 6]])
    # 1 3
    # 4 6
    
    A_log = torch.ByteTensor([1, 0, 1]) # the logical index
    B = torch.LongTensor([[1, 2, 3], [4, 5, 6]])
    
    # Convert the logical index tensor to a boolean mask
    mask = A_log.bool()
    
    # Use the boolean mask for indexing
    C = B[:, mask]
    
    print(C)
    


### END SOLUTION
C = solve(A_log, B)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(C, f)
