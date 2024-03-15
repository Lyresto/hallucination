import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd


index = pd.MultiIndex.from_tuples([('abc', '3/1/1994'), ('abc', '9/1/1994'), ('abc', '3/1/1995')],
                                 names=('id', 'date'))
df = pd.DataFrame({'x': [100, 90, 80], 'y':[7, 8, 9]}, index=index)

###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)