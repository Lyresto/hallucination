import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
df['index'] = df.index
df['Random'] = df.groupby('UserId')['index'].transform(lambda x: x.sample(frac=0.2, random_state=0))
df.loc[df['Random'].notnull(), 'Quantity'] = 0
df = df.drop(['index', 'Random'], axis=1)



###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)