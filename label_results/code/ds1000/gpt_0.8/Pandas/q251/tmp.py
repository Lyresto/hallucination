import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
df['code_0'] = df['codes'].apply(lambda x: x[0] if len(x) > 0 else None)
df['code_1'] = df['codes'].apply(lambda x: x[1] if len(x) > 1 else None)
df['code_2'] = df['codes'].apply(lambda x: x[2] if len(x) > 2 else None)
result = df.drop('codes', axis=1)



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)