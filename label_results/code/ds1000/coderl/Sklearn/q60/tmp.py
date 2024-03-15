import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
import sklearn

features = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
from numpy import array




def gen_selection(features):
    vector = array([[0] * len(f) for f in features[0]])
    for i, f in enumerate(features[1:]):
        for j in range(len(f)):
            vector[i + 1][j] = 1
    return vector



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(new_features, f)
