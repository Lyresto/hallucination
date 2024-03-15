import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION



def df_exp(df,col,prefix):
    ans = ""
    for i in df.columns:
        if i == col:
            ans += prefix+"_"+str(i)
        else:
            ans += prefix+"^"+str(i)
    return ans



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)