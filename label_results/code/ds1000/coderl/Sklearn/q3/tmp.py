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



def solve(data):
    # return the solution in this function
    # result = solve(data)
    # ### BEGIN SOLUTION
    iris = data['data']
    # pd.DataFrame(iris)
    return pd.DataFrame(iris).values



### END SOLUTION
data1 = solve(data)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(data1, f)
