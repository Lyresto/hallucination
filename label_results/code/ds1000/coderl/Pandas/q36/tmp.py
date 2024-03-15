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




def mean_advance(df, row_list, column_list, axis):
    if len(row_list) == 0:
        return 0
    result = []
    for row in range(len(row_list)):
        mean = sum(df[col] for col in column_list) / len(column_list)
        result.append(mean)
    return mean(result)



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)