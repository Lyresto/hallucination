import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df1 = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
slopes = np.array([])
for col in df1.columns:
    if col != 'Time':
        df2 = df1[~np.isnan(df1[col])]
        df3 = df2[['Time', col]]
        npMatrix = np.matrix(df3)
        X, Y = npMatrix[:,0], npMatrix[:,1]
        slope = LinearRegression().fit(X,Y)
        m = slope.coef_[0]
        slopes = np.concatenate((slopes, m), axis = 0)

### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(slopes, f)
