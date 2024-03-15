import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
df = pd.DataFrame({'Sp': ['MM1', 'MM1', 'MM1', 'MM2', 'MM2', 'MM2', 'MM4', 'MM4', 'MM4'],
                   'Mt': ['S1', 'S1', 'S3', 'S3', 'S4', 'S4', 'S2', 'S2', 'S2'],
                   'Value': ['a', 'n', 'cb','mk', 'bg', 'dgd', 'rd', 'cb', 'uyi'],
                   'count': [3, 2, 5, 8, 10, 1, 2, 2, 7]})

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)