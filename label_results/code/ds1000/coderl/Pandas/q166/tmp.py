import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION



def stdMeann(df):
    s = [0]*len(df)
    for i in range(len(df)):
        s[i] = df['b'].mean()
        s[i+1] = df['b'].std()
    return pd.Series(s)



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)