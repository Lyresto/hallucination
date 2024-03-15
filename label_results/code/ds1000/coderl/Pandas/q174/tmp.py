import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

s = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION



def df_from_series(s):
    series = list(s.sort_values(by=lambda x: x.split('t'))[:-5:-1])
    index = list(s.index.values[:-5:-1])
    return pd.DataFrame(series, index=index)



###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)