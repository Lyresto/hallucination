import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
result = df.drop_duplicates(subset='url', keep='last')
result = result.groupby('url').apply(lambda x: x if 'Yes' in x['keep_if_dup'].values else x.drop_duplicates(subset='keep_if_dup', keep='last'))
result = result.reset_index(drop=True)

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)