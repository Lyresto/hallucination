import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df, thresh = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
from statistics import mean




def df_greater_than(df, thresh):
    return sum(mean(df.loc[row] for row in range(len(df)) if df.loc[row]['value'] > thresh) for row in range(len(df))) * thresh ** 2 



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)