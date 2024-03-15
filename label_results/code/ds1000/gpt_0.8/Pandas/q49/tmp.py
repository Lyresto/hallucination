import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df, section_left, section_right = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
mask = (df['value'] < section_left) | (df['value'] > section_right)
avg = df.loc[mask, 'value'].mean()
df.loc[~mask, 'value'] = avg
df = df.groupby(df.index).first() # remove duplicates
df = df.reset_index()
df.loc[df['value'] == avg, 'lab'] = 'X'
df = df.groupby('lab').sum()



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)