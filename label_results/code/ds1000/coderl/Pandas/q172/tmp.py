import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION



def fill_column(df, column):
    if column in df.columns:
        df[column] = df[column].fillna(value=0)
    else:
        df[column] = 0
    return df




def fill_rows(df):
    for row in df.values:
        row.fillna(value=0,inplace=True)
    return df



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)