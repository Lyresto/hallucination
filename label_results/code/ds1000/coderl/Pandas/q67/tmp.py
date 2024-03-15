import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
from itertools import zip_longest
from typing import List
import pandas as pd





def pivot_table(df: pd.DataFrame, pivot_by: List[str] = ['user', 'date', 'value'], output_columns: List[str] = ['user', 'date', 'value','someBool']):
    # x-array = list(zip_longest(*([df.ix[:, x] for x in range(0, len(df))], fillvalue=0)))
    x-array = df.pivot(index='user', columns=pivot_by, values='date')
    y-array = df.pivot(index='date', columns=pivot_by, values='value')
    return pd.concat(xarray, yarray, axis=1, join='outer')



###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)