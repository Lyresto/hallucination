import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df, bins = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
result = pd.pivot_table(df, index='username', columns=pd.cut(df.views, bins), values='post_id', aggfunc='count')
result.columns = [f'{str(c.left)}-{str(c.right)}' for c in result.columns]

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)