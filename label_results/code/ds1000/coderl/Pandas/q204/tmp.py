import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np




def f(df):
    ### BEGIN SOLUTION



def f(df=example_df):
    total = 0
    for i, r in enumerate(df.values):
        total += r
    return total / len(df)



    ### END SOLUTION


df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = f(df)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)