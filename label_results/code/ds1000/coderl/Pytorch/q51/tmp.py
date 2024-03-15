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
    from collections import Counter
    
    


def load_data():
    a = np.array([i for i in range(1000)], dtype = np.int64)
    b = np.array([i for i in range(1000)], dtype = np.int64)
    a, b = a.reshape(-1, 1), b.reshape(-1, 1)
    return a == b
    



def Count(a, b):
    c = Counter(a) == Counter(b)
    return c.sum()



### END SOLUTION
cnt_equal = Count(A, B)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(cnt_equal, f)
