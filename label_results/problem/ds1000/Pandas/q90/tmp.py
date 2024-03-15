import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df1, df2, columns_check_list = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
# One solution is to use a loop to iterate over the columns_check_list and build the condition step by step
condition = df1[columns_check_list[0]] == df2[columns_check_list[0]]
for column in columns_check_list[1:]:
    condition = condition & (df1[column] == df2[column])
result = list(condition)

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)