import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df, section_left, section_right = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
from pandas import DataFrame



def aggregate_rows_not_in_a_section(df, section_left, section_right):
    lab_vals = df.loc[:section_left, 'lab'].values.tolist()
    value_vals = df.loc[section_left:section_right, 'value'].values.tolist()
    return (sum(value_vals)/len(value_vals)) if value_vals else (sum(lab_vals)/len(lab_vals))



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)