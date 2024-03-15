import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
df = df.groupby('UserId').apply(lambda x: x.sample(frac=0.2, random_state=0))
df['Quantity'] = df['Quantity'].apply(lambda x: 0 if x != 0 else x)
df = df.reset_index(drop=True)

###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)