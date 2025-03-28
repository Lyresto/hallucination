import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np




def f(df, columns):
    ### BEGIN SOLUTION



def f(df, columns=['b', 'e']):
    return sum(df[c].sum() for c in columns if df[c].max() > 0.5)



    ### END SOLUTION

df, columns = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = f(df, columns)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)