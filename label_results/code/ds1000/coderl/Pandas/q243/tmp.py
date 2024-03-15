import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
from pandas import groupby




def agg(df):
    result = []
    for key, group in groupby(df, key = lambda x: x[0]):
        group_list = list(group.tolist())
        result.append(list(zip(group['time'], group_list)))
    return pd.DataFrame(result)



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)