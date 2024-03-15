import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df,List = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
df = df[(df['Date'] >= List[0]) & (df['Date'] <= List[1])]
df['Month'] = df['Date'].dt.month_name().str.slice(stop=3)
df['Year'] = df['Date'].dt.year
df['Day'] = df['Date'].dt.day_name().str.slice(stop=3)
df['Date'] = df['Month'] + '-' + df['Day'] + '-' + df['Year'].astype(str)
df = df[['Date']]



###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)