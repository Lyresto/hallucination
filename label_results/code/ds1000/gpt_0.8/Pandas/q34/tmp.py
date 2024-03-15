import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
# Solution 1: using filter() to select columns with 'val' in their name
result = df.groupby('group').agg({"group_color": "first"})
result = result.join(df.filter(like='val').sum(axis=1).rename('val_sum'))



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)