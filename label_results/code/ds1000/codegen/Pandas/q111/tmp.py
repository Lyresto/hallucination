import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd


df = pd.DataFrame({'datetime': ['2021-04-10 01:00:00', '2021-04-10 02:00:00', '2021-04-10 03:00:00', '2021-04-10 04:00:00', '2021-04-10 05:00:00'],
                   'col1': [25, 25, 25, 50, 100],
                   'col2': [50, 50, 100, 50, 100],
                   'col3': [50, 50, 50, 100, 100]})


df['datetime'] = pd.to_datetime(df['datetime'])

###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)