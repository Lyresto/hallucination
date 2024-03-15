import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
# Get all column names that contain 'val'
val_cols = [col for col in df.columns if 'val' in col]

# Get a dictionary with the mean aggregation for each value column
agg_dict = {col: 'mean' for col in val_cols}

# Add 'group_color' to the dictionary to make sure it stays in the result
agg_dict['group_color'] = 'first'

# Group by 'group' and aggregate using the agg_dict
result = df.groupby('group').agg(agg_dict)



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)