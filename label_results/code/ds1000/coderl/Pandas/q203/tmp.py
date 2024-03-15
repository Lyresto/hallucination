import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
from statistics import mean




def mean_value(frame, key):
    return mean([frame[key].max(), frame[key].min()][:-1])




def mean_columns(frame):
    return str([mean_value(frame, key) for key in frame.columns])




def mean_rows(frame):
    return str([mean_value(frame, key) for key in frame.index])




def __starting_point():
    df = pd.read_csv('input.txt', sep=' ', header=None)
    print(mean_columns(df))
    print(mean_rows(df))

__starting_point()



###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)