import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

np_array = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
def Transform(a):
### BEGIN SOLUTION
    scaler = MinMaxScaler()
    new_a = scaler.fit_transform(a.reshape(-1,1)).reshape(a.shape)
    return new_a
    ### END SOLUTION
### END SOLUTION
transformed = Transform(np_array)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(transformed, f)
