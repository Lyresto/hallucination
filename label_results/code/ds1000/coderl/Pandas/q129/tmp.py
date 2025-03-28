import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION



def rand_select(df):
    s = df.sample(int(len(df)*0.8), random_state=0)
    res = {}
    for i, row in enumerate(s):
        res["UserId"] = row["UserId"]
        res["ProductId"] = row["ProductId"]
        res["Quantity"] = row["Quantity"]
    return res



###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)