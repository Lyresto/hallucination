import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df, thresh = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
# select the rows to be aggregated
agg_rows = df.loc[df['value'] >= thresh]

# compute the average value of the selected rows
avg_value = agg_rows['value'].mean()

# create a new row with the computed average value and label it as 'X'
new_row = pd.DataFrame({'value': [avg_value]}, index=['X'])

# drop the selected rows from the original dataframe
df = df.drop(agg_rows.index)

# add the new row to the dataframe
df = pd.concat([df, new_row])

# sort the dataframe by index
df = df.sort_index()



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)