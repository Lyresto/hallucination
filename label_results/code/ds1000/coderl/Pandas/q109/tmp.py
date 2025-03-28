import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df1, df2 = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION



def time_spent(df1, df2):
    return df1['Timestamp'] - df2['Timestamp']



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)