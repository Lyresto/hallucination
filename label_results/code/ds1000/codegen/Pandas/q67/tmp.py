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

df = pd.DataFrame({'user': ['u1', 'u2', 'u3'],
                   '01/12/15': [100, 200, None],
                   '02/12/15': [None, -100, 200],
                  'someBool': [True, False, True]})

###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)