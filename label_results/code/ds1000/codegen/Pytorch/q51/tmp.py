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

    cnt_equal = np.count_nonzero(A == B)
    ### END SOLUTION
    return cnt_equal

def load_data():
    #
### END SOLUTION
cnt_equal = Count(A, B)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(cnt_equal, f)
