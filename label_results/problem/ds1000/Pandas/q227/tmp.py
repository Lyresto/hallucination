import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

a,b,c = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
# One way to solve this is to use the zip function to combine the dataframes and then apply the tuple function to each row

dfs = [a, b, c] # list of dataframes
zipped = zip(*dfs) # combine the dataframes
result = pd.DataFrame([tuple(row) for row in zipped], columns=a.columns) # apply tuple function to each row and create dataframe

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)