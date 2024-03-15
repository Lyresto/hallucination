import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import dask.dataframe as dd

# Read the CSV file into a Dask DataFrame
df = dd.read_csv('file.csv')

# Split the 'var2' column into multiple rows
df = df.assign(var2=df['var2'].str.split(','))

# Explode the 'var2' column into multiple rows
df = df.explode('var2')

# Reset the index
df = df.reset_index(drop=True)

# Display the resulting Dask DataFrame
df.compute()



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)