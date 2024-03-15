import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
# First, replace all 0 values with NaN
df.replace(0, pd.np.nan, inplace=True)

# Then, calculate the cumulative sum for each row from end to head
cumulative_sum = df.iloc[:, 1:].iloc[:, ::-1].cumsum(axis=1).iloc[:, ::-1]

# Calculate the number of non-zero values for each row
non_zero_count = df.iloc[:, 1:].apply(lambda x: x[x.notnull()].count(), axis=1)

# Calculate the cumulative average for each row from end to head
cumulative_avg = cumulative_sum.div(non_zero_count, axis=0)

# Replace NaN values with 0
cumulative_avg.fillna(0, inplace=True)

# Combine the Name column with the cumulative average dataframe
df = pd.concat([df['Name'], cumulative_avg], axis=1)

###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)