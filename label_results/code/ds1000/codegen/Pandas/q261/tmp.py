import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
df = pd.DataFrame({'ID': ['01', '01', '01', '02', '02'],
                   'TIME': ['2018-07-11 11:12:20', '2018-07-12 12:00:23', '2018-07-13 12:00:00', '2019-09-11 11:00:00', '2019-09-12 12:00:00']})

###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)