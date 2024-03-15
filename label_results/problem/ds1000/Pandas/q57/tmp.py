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
dates = pd.date_range(start=min_date, end=max_date)
users = df['user'].unique()
new_df = pd.DataFrame({'dt': dates})
for user in users:
    user_df = df[df['user']==user]
    user_df = user_df.set_index('dt')
    user_df = user_df.reindex(dates)
    user_df['user'] = user
    user_df['val'] = user_df['val'].fillna(0)
    new_df = pd.concat([new_df, user_df.reset_index()], axis=0)
new_df = new_df[['dt', 'user', 'val']]

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)