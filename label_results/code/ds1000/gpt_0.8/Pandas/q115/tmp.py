import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
df['total'] = df.sum(axis=1)
df.loc[:, 'val1':'val4'] = df.loc[:, 'val1':'val4'].div(df['total'], axis=0)
df = df.drop(columns='total')
df


###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)