import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd


df = pd.DataFrame({'cat': ['A', 'B', 'C'],
                   'val1': [7, 10, 5],
                   'val2': [10, 2, 15],
                   'val3': [0, 1, 6],
                   'val4': [19, 14, 16]})

###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)