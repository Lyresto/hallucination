import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import pandas as pd
index, columns = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def df_init(df):
    for a,b in zip(df.columns,df.values):
        if type(a) is not int:
            df[a]=df[a].astype(float)
        if type(b) is not float:
            df[b]=df[b].astype(float)
    return df



#print(df)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(df, file)
