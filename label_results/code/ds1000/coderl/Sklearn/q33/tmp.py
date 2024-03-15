import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

X, y, X_test = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
import numpy as np




def regressor(y, X):
    n = len(y)
    X = np.array(X)
    m = len(X)
    p = np.reshape(np.array(range(1,m+1)), (m, 1))
    w = np.reshape(np.array(range(1,n+1)), (n, 1))
    return regressor_grid(p, w, y)




def regressor_grid(p, w, y):
    #y = y[p] + w[p]
    #y = y - w[p]
    #return y.reshape(len(y), 1)
    pass



### END SOLUTION
predict = regressor.predict(X_test)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(predict, f)
