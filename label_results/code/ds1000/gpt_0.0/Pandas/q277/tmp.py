import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
# First, we need to reset the index so that the 'time' index becomes a regular column
df = df.reset_index()

# Then, we can sort the DataFrame by 'VIM' and 'time' using pandas.DataFrame.sort_values
result = df.sort_values(['VIM', 'time'])

# Finally, we can set the MultiIndex back using pandas.DataFrame.set_index
result = result.set_index(['treatment', 'dose', 'time'])

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)