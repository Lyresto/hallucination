import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

a,b = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
# First, create a list of the dataframes
dfs = [a, b]

# Find the maximum length of the dataframes
max_len = max([len(df) for df in dfs])

# Create a dictionary to store the columns
cols = {}

# Loop through each dataframe
for i, df in enumerate(dfs):
    # Loop through each column in the dataframe
    for col in df.columns:
        # Create a list to store the values for this column
        col_values = []
        # Loop through each row in the dataframe
        for j in range(max_len):
            # If the row exists, append the value to the list
            if j < len(df):
                col_values.append(df.loc[j, col])
            # Otherwise, append np.nan
            else:
                col_values.append(np.nan)
        # Add the column to the dictionary
        cols[(i, col)] = col_values

# Create a new dataframe from the dictionary
result = pd.DataFrame(cols)

# Convert the tuples to columns
result.columns = pd.MultiIndex.from_tuples(result.columns)
result = result.applymap(lambda x: tuple(x))

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)