import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
# Get all columns that contain "val" in their name
val_cols = [col for col in df.columns if "val" in col]

# Group by "group" column and take the mean of all value columns
result = df.groupby("group")[val_cols].mean().reset_index()

# Add the first value of "group_color" column to the result
result["group_color"] = df.groupby("group")["group_color"].first().values

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)