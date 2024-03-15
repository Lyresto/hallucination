import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df, row_list, column_list = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd



def df_sum_advance(df, row_list, column_list, axis=0):
    result = []
    for i in range(len(row_list)):
        result.append(sum(df[row] for row in row_list[i:]))
    return sum(result, axis=axis)



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)