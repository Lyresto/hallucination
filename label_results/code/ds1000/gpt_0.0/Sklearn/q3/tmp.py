import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

data = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
def solve(data):
### BEGIN SOLUTION
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = pd.Series(data.target)
    return df
    ### END SOLUTION
### END SOLUTION
data1 = solve(data)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(data1, f)
