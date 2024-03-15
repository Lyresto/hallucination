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

regressor = RandomForestRegressor(n_estimators=150, min_samples_split=1.0, random_state=42)
rgr = regressor.fit(X,y)
predict = rgr.predict(X_test)

### END SOLUTION
predict = regressor.predict(X_test)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(predict, f)
