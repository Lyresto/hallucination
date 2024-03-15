import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION



def to_series(df):
    from datetime import datetime
    d = []
    for i,j in df.iteritems():
        d.append(datetime.strptime(i, '%Y-%m-%d'))
    return df.assign(Value=lambda a,b:sum(b)*a,Date=d)



###END SOLUTION
result = ts

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)