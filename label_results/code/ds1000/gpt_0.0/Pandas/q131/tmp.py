import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
# First, we need to find the index of the last occurrence of each duplicate
last_occurrence = df.duplicated(subset=['col1','col2'], keep='last')

# Then, we can use the groupby method to get the index of the last occurrence for each group of duplicates
last_index = df[last_occurrence].groupby(['col1','col2']).tail(1).index

# Finally, we can create a new column in the duplicate dataframe with the index of the last occurrence
duplicate = df[last_occurrence].copy()
duplicate['index_original'] = last_index

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)