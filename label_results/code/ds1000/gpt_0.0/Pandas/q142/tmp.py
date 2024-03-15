import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
# First, we need to create a list of tuples that specifies the column levels we want to melt
# We can do this by iterating over the levels of the columns MultiIndex and creating a tuple for each combination
# of levels
col_tuples = []
for i in range(df.columns.nlevels):
    for j in range(i+1, df.columns.nlevels):
        for k in range(df.columns.nlevels):
            col_tuples.append((df.columns.names[i], df.columns.names[j], df.columns.names[k]))

# Then, we can pass this list of tuples to the value_vars parameter of pd.melt
result = pd.melt(df, id_vars=[], value_vars=col_tuples, var_name=['variable_0', 'variable_1', 'variable_2'], value_name='value')

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)