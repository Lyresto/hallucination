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
df1 = load_data()
slopes =... # put solution in this variable
df1 = df1[~np.isnan(df1['A1'])]
df2 = df1[['Time','A1']]
npMatrix = np.matrix(df2)
X, Y = npMatrix[:,0], npMatrix[:,1]
slope = LinearRegression().fit(X,Y)
m = slope.coef_[0]
series= np.concatenate((SGR_trips, m), axis = 0)

### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(slopes, f)
