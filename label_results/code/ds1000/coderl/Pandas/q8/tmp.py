import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
from collections import OrderedDict




def drop_duplicates(df, drop_if_dup=None):
    d = OrderedDict()
    for i, j in df.iterrows():
        d[j['url']] = i
        if drop_if_dup is not None and i == d[drop_if_dup]:
            return None
    return df.replace(d, None)



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)