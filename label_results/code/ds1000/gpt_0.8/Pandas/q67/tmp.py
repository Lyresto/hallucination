import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
df = pd.melt(df, id_vars=['user', 'someBool'], var_name='date', value_name='value')
df = df.dropna() # remove rows with missing values
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%y') # convert date column to datetime format
df = df.sort_values(by=['user', 'date']) # sort by user and date
df = df.reset_index(drop=True) # reset index



###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)