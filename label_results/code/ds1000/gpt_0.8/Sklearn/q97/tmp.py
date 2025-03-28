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
    normalized_array = scaler.fit_transform(np_array.flatten().reshape(-1, 1))
    new_a = normalized_array.reshape(np_array.shape)
    ### END SOLUTION
    return new_a


### END SOLUTION
transformed = Transform(np_array)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(transformed, f)
