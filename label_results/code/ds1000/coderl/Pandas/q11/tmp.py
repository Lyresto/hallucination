import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd




def tz_localize(datetime):
    t = datetime.split(' ')
    s = str(t[0]) +'' + t[1][:2] +'' + t[1][3:]
    t[0] = s[:-3]
    t[1] = s[-3:]
    return pd.to_datetime(t)



###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)