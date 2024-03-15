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


df = pd.DataFrame({'col1': {0: 'a', 1: 'b', 2: 'c'},
                   'col2': {0: 1, 1: 3, 2: 5},
                   'col3': {0: 2, 1: 4, 2: 6},
                   'col4': {0: 3, 1: 6, 2: 2},
                   'col5': {0: 7, 1: 2, 2: 3},
                   'col6': {0: 2, 1: 9, 2: 5},
                  })
df.columns = [list('AAAAAA'), list('BBCCDD'), list('EFGHIJ')]

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)