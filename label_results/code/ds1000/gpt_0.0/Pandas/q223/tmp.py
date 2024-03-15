import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
# Count the number of NaN values in the column
num_nan = df['Column_x'].isna().sum()

# Calculate the number of NaN values to fill with 0 and 1
num_fill_0 = num_nan // 2
num_fill_1 = num_nan - num_fill_0

# Create a list of values to fill NaN with
fill_values = [0] * num_fill_0 + [1] * num_fill_1

# Shuffle the list to randomize the order of filling NaN values
np.random.shuffle(fill_values)

# Create a boolean mask for NaN values in the column
nan_mask = df['Column_x'].isna()

# Fill NaN values with the values from the shuffled list
df.loc[nan_mask, 'Column_x'] = fill_values

# Convert the column to integer type
df['Column_x'] = df['Column_x'].astype(int)

###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)