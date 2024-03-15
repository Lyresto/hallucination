import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df, section_left, section_right = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd

df = pd.DataFrame({'lab':['A', 'B', 'C', 'D', 'E', 'F'], 'value':[50, 35, 8, 5, 1, 1]})
df = df.set_index('lab')
section_left = 4
section_right = 38

df = df.loc[df['value'] > section_left]
df = df.loc[df['value'] < section_right]

df = df.loc[df['value'] == section_left]
df = df.loc[df['value'] == section_right]

df = df.loc[df['value'] == section_left]
df = df.loc[df['value'] == section_right]

df = df.loc[df['value'] == section_left]
df = df.loc[df['value'] == section_right]

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)