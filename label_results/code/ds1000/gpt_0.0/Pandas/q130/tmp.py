import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
df['index_original'] = df.index
duplicate_bool = df.duplicated(subset=['col1','col2'], keep='first')
result = df.loc[duplicate_bool == True]
result = result.merge(df[['col1','col2','index_original']], on=['col1','col2'], how='left')
result = result[['col1','col2','index_original']]

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)