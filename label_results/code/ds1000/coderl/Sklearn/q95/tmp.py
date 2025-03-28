import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

np_array = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION



def minmax_scaler(a):
    m = MinMaxScaler()
    return m.fit_transform(a).tolist()



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(transformed, f)
