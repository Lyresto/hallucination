import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import numpy as np
import pandas as pd
import torch

A, B = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def Count(A, B):
### BEGIN SOLUTION
    import torch
    
    


def count_equal_elements(A, B):
    # Check for element-wise equality
    equal_elements = torch.eq(A, B)
    
    # Count the number of equal elements
    count = torch.sum(equal_elements).item()
    
    return count



### END SOLUTION
cnt_equal = Count(A, B)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(cnt_equal, f)
