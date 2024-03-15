import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df, filt = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION



def filter_dataframe(df, filt):
    if len(df.index.levels)!= len(filt.index.levels):
        return False
    new_df = df.copy()
    for i,v in enumerate(df.index.levels):
        if v is not None:
            new_df.ix[i,v] = df.ix[i,v]
    for i,v in enumerate(filt.index.levels):
        if v is not None:
            new_df.ix[i,v] = filt.ix[i,v]
    return new_df



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)