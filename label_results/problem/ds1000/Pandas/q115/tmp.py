import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
# Compute row totals
row_totals = df.iloc[:, 1:].sum(axis=1)

# Divide each value by its corresponding row total
df.iloc[:, 1:] = df.iloc[:, 1:].div(row_totals, axis=0)

# Round to 3 decimal places
df.iloc[:, 1:] = df.iloc[:, 1:].round(3)

# Rename columns
df.columns = ['cat', 'val1%', 'val2%', 'val3%', 'val4%']

###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)