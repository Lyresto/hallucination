import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df, filt = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd


df = pd.DataFrame({'a': [1,1,1,2,2,2,3,3,3],
                    'b': [1,2,3,1,2,3,1,2,3],
                    'c': range(9)}).set_index(['a', 'b'])
filt = pd.Series({1:True, 2:False, 3:True})

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)