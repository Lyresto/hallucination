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




def split_df(df):
    fips = ['row']
    for i in range(len(df.row)):
        fips.append(df.row[i].split(' ', 1)[0])
    return pd.DataFrame({'fips': fips, 'row': df.row})



###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)