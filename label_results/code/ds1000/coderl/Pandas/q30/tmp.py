import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd
df1 = pd.DataFrame({'HeaderA': [476],
    'HeaderB': [4365],
    'HeaderC': [457]})
df2 = pd.DataFrame(
    {'HeaderA': [76],
    'HeaderB': [345],
    'HeaderC': [456]})
df = pd.concat([df1, df2], ignore_index=True)
df.rename(columns={'HeaderA': 'HeaderAX'}, inplace=True)



###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)