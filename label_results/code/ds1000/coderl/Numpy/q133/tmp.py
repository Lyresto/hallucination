import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import pandas as pd
names, times, df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
from datetime import datetime




def to_numpy_array(df):
    df_t = df.to_dict()
    df_t["major"] = df_t["major"].astype(float)
    arr = [[df_t[str(i)][j] for j in range(5)] for i in range(15)]
    return np.array(arr)



#print(result)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
