import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
df['Column_x'] = df['Column_x'].fillna(0)  # Fill first 50% with 0
nan_count = df['Column_x'].isnull().sum()  # Count remaining NaN values
df['Column_x'] = df['Column_x'].fillna(1, limit=nan_count)  # Fill remaining NaN values with 1



###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)