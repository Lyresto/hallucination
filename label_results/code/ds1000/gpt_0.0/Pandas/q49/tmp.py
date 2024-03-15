import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df, section_left, section_right = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
# First, we create a mask to identify the rows that are not in the given section
mask = (df['value'] < section_left) | (df['value'] > section_right)

# Then, we calculate the average of the rows that will be substituted
avg = df.loc[~mask, 'value'].mean()

# We create a new row with the average value and a label to identify the substituted rows
new_row = pd.DataFrame({'lab':['X'], 'value':[avg]})

# Finally, we replace the rows that are not in the section with the new row
df.loc[~mask] = new_row.values

result = df

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)