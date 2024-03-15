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




def melt(df, value_vars):
    new_cols = list(df.columns)
    for i, v in enumerate(value_vars):
        new_cols[i] = [v[0] for _ in range(len(v))] + v[1:]
    return pd.melt(df, new_cols)



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)