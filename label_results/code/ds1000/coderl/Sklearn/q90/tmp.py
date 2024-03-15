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
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

slopes = []
for col in df1.columns:
    df2 = df1[~np.isnan(df1[col])]
    npMatrix = np.matrix(df2)
    X, Y = npMatrix[:, 0], npMatrix[:, 1]
    slope = LinearRegression().fit(X,Y)
    m = slope.coef_[0]
    slopes.append(m)

df1['Z3'] =lopes[0]




### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(slopes, f)
