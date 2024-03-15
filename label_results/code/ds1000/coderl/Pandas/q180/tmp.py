import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
from collections import defaultdict
from itertools import groupby




def maxcount(df):
    dct = defaultdict(list)
    for k, v in groupby(df, 'Value'):
        dct[k].append(v.max())
    return [len(list(v)) for k, v in dct.items()]


rows = maxcount(pd.DataFrame({'Sp': ['a', 'a', 'n', 'cb','mk', 'bg', 'dgd', 'rd', 'cb', 'uyi'],
                             'Value': ['S1', 'S1', 'S3', 'S3', 'S4', 'S4', 'S2', 'S2', 'S2'],
                             'Mt': ['a', 'n', 'cb','mk', 'bg', 'dgd', 'rd', 'cb', 'uyi'],
                             'count': [3,2,5,8,10,1,2,2,7]}))



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)