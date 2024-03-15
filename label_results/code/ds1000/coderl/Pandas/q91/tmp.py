import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import datetime as dt
from itertools import chain, zip_longest




def parse_date(dates):
    for i, d in zip_longest(*zip_longest(*[iter(dates)] * 2)):
        try:
            i = dt.strptime(d, '%Y/%m/%d')
            yield i
        except ValueError:
            pass




def __starting_point():
    df = pd.DataFrame({'x': [100, 90, 80], 'y':[7, 8, 9]}, index=['abc', '3/1/1994', '3/1/1995'])
    print(df.index.levels[1])
    for i, j in parse_date(df.index.levels[1]):
        print(i, j)
    print(df.index.levels[1])

__starting_point()



###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)