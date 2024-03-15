import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
from collections import defaultdict




def find_duplicated_rows(df):
    df = df.sort_values(by=['col1', 'col2'])
    result = defaultdict(list)
    for row in df:
        result[row[0]].append(row[1])
    for col in result:
        result[col].sort()
    for row, col_index in result.items():
        df.loc[row, col] = df.loc[col, col_index].values.pop()
    return df



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)