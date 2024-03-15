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
    import torch
    
    a = torch.Tensor([[1, 2, 3], [1, 2, 3]])
    b = torch.Tensor([[5, 6, 7], [5, 6, 7]])
    
    # Get the number of rows and columns in a and b
    num_rows, num_cols_a = a.shape
    _, num_cols_b = b.shape
    
    # Calculate the number of overlapping columns
    overlap_cols = min(num_cols_a, num_cols_b - 1)
    
    # Slice the columns from a and b for the result tensor
    result_a = a[:, :num_cols_a - overlap_cols]
    result_b = b[:, overlap_cols:]
    
    # Calculate the average column
    average_col = (a[:, num_cols_a - 1] + b[:, 0]) / 2
    
    # Concatenate the tensors to form the result
    result = torch.cat((result_a, average_col.unsqueeze(1), result_b), dim=1)
    
    print(result)
    


### END SOLUTION
result = solve(a, b)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
