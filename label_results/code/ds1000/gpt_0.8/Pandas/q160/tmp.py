import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
df_sorted = df.groupby('cokey').apply(lambda x: x.sort_values('A'))
result = df_sorted.reset_index(drop=True)



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)