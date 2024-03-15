import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd

df = pd.DataFrame({'Name': ['Name1', 'Name2', 'Name3'],
                   '2001': [2, 1, 0],
                   '2002': [5, 4, 5],
                   '2003': [0, 2, 0],
                   '2004': [0, 0, 0],
                   '2005': [4, 4, 0],
                   '2006': [6, 0, 2]})

# Reversing the order of columns
df = df.iloc[:, ::-1]

# Calculate cumulative average while ignoring zero values
df = df.apply(lambda x: x.cumsum() / x.replace(0, pd.NA).ffill(), axis=1)

# Reversing the order of columns back to original
df = df.iloc[:, ::-1]

df



###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)