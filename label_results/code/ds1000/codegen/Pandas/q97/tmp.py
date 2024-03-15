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


df = pd.DataFrame({'A_Name': ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG'],
                   'B_Detail': ['X1', 'Y1', 'Z1', 'L1', 'M1', 'N1', 'K1'],
                   'Value_B': [1.2, 0.76, 0.7, 0.9, 1.3, 0.7, -2.4],
                   'Value_C': [0.5, -0.7, -1.3, -0.5, 1.8, -0.8, -1.9],
                   'Value_D': [-1.3, 0.8, 2.5, 0.4, -1.3, 0.9, 2.1]})

###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)