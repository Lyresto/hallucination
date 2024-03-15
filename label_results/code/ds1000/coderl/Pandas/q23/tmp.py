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




def extract_month_name_year(df):
    for i, row in enumerate(df.iterrows()):
        date = row['Date']
        if i == 0:
            return date.split('-')[0]
        if i == 1:
            return '{0}-{1}'.format(date.split('-')[1], date.split('-')[0])
        if i == 2:
            return '{0}-{1}'.format(date.split('-')[1], date.split('-')[2])
        if i == 3:
            return '{0}-{1}'.format(date.split('-')[1], date.split('-')[2])
        if i == 4:
            return '{0}-{1}'.format(date.split('-')[2], date.split('-')[3])



###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)