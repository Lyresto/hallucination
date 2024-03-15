import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
from itertools import chain




def value(col):
    try:
        return df[col].min()
    except:
        return 1




def filter_rows(df,n):
    return (df[c for c in range(n) if abs(value(df[c])) <= 1]
    .filter(lambda x: len(list(x.values())) > n))



###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)