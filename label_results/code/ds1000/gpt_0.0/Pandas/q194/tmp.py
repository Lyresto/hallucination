import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import dask.dataframe as dd
from dask import compute, delayed

df = dd.from_pandas(df, npartitions=2)

def split_rows(row):
    var1 = row['var1']
    var2 = row['var2'].split(',')
    return [(row['id'], var1, v) for v in var2]

new_rows = []
for _, row in df.iterrows():
    new_rows.extend(split_rows(row))

result = dd.from_delayed(new_rows, meta=('id', 'var1', 'var2'))
result = result.set_index('id')

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)