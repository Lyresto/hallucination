import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
# Get all columns starting with 'Value'
value_cols = [col for col in df.columns if col.startswith('Value')]

# Filter rows where absolute value of all 'Value' columns is less than 1
df = df[(df[value_cols].abs() < 1).all(axis=1)]

###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)