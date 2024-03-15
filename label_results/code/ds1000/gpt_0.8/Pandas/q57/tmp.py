import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
min_date = df['dt'].min()
max_date = df['dt'].max()
idx = pd.date_range(min_date, max_date)
users = df['user'].unique()
result = pd.DataFrame({'dt': idx})
for user in users:
    user_df = df[df['user'] == user].set_index('dt')
    user_df = user_df.reindex(idx, fill_value=0)
    user_df.reset_index(inplace=True)
    user_df['user'] = user
    result = pd.concat([result, user_df[['user', 'dt', 'val']]], ignore_index=True)



###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)