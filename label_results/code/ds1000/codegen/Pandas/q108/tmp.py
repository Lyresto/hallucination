import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df1, df2 = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
df1 = pd.DataFrame({'Timestamp': ['2019/04/02 11:00:01', '2019/04/02 11:00:15', '2019/04/02 11:00:29', '2019/04/02 11:00:30'],
                    'data': [111, 222, 333, 444]})
df2 = pd.DataFrame({'Timestamp': ['2019/04/02 11:00:14', '2019/04/02 11:00:15', '2019/04/02 11:00:16', '2019/04/02 11:00:30', '2019/04/02 11:00:31'],
                   'stuff': [101, 202, 303, 404, 505]})
df1['Timestamp'] = pd.to_datetime(df1['Timestamp'])
df2['Timestamp'] = pd.to_datetime(df2['Timestamp'])

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)