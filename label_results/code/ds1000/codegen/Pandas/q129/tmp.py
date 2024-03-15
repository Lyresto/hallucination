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


df = pd.DataFrame({'UserId': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3],
                   'ProductId': [1, 4, 7, 4, 2, 1, 1, 4, 7, 4, 2, 1, 1, 4, 7],
                   'Quantity': [6, 1, 3, 2, 7, 2, 6, 1, 3, 2, 7, 2, 6, 1, 3]})

###END SOLUTION
result = df

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)