import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
result = df.groupby('a').agg({'b': ['mean', 'std']})
result.columns = result.columns.droplevel()
result = result.rename(columns={'mean': 'mean_b', 'std': 'std_b'})
result = result.reset_index()

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)