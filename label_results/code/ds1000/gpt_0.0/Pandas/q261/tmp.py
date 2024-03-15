import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
# Convert TIME column to datetime format
df['TIME'] = pd.to_datetime(df['TIME'])

# Add a new column for formatted time
df['FORMATTED_TIME'] = df['TIME'].dt.strftime('%d-%b-%Y %a %H:%M:%S')

# Add a new column for ranking by ID and TIME
df['RANK'] = df.groupby('ID')['TIME'].rank(ascending=False)

###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)