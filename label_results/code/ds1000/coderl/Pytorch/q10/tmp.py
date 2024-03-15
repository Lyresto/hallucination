import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import numpy as np
import pandas as pd
import torch

A_logical, B = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
import pandas as pd
import torch




def load_data():
    a, b = pd.read_csv('../../data/input.csv')['A'].values, pd.read_csv('../../data/input.csv')['B'].values
    a = a.astype(np.int64)
    b = b.astype(np.int64)
    return a[b == 1], b



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(C, f)
