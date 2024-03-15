import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
# Solution for deleting particular days
dates_to_delete = ['2020-02-17', '2020-02-18']
for date in dates_to_delete:
    df = df[df.index.date != pd.to_datetime(date).date()]

# Solution for converting date to desired format
df['DayOfWeek'] = df.index.strftime('%d-%b-%Y %A')
df = df[['DayOfWeek'] + list(df.columns[:-1])]
END SOLUTION
###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)