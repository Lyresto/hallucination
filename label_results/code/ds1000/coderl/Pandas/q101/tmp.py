import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import re



def replace(s):
    return re.sub(r'[&lt;]{2,}[\s,;]*', '<', s)
    



def replace_all(df):
    for i, c in df.iteritems():
        df[i] = replace(c)
    return df



###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)