import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=list('ABA'))
df.columns = ['A', 'B', 'C']
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.columns.name = 'Test'
df.column
###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)