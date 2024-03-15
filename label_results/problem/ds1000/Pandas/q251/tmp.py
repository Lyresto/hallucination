import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
# First, find the maximum length of any list in the 'codes' column
max_len = max(df['codes'].apply(len))

# Create a new dataframe with columns for each code index
new_df = pd.DataFrame(df['codes'].tolist(), columns=[f'code_{i}' for i in range(max_len)])

# Concatenate the new dataframe with the original dataframe
result = pd.concat([df, new_df], axis=1).drop('codes', axis=1)

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)