import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df,List = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import re




def extract_date(df, list):
    for i in range(len(list)):
        df['Date'] = re.sub(r'\d{2}-\d{2}-\d{4}', lambda m: f'{m.group(0)}-{m.group(1)}', df['Date'])
    return df['Date'][0:10]



###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)