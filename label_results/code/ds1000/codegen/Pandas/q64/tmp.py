import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
df = pd.DataFrame({'name': ['Aaron', 'Aaron', 'Aaron', 'Brave', 'Brave', 'David'],
                   'a': [3, 3, 3, 4, 3, 5],
                   'b': [5, 6, 6, 6, 6, 1],
                   'c': [7, 9, 10, 0, 1, 4]})

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)