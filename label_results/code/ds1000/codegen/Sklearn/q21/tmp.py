import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
import xgboost.sklearn as xgb
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import TimeSeriesSplit

gridsearch, testX, testY, trainX, trainY = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION

import numpy as np
import pandas as pd
import xgboost.sklearn as xgb
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import TimeSeriesSplit
gridsearch, testX, testY, trainX, trainY = load_data()
assert type(gridsearch) == sklearn.model_selection._search.GridSearchCV
assert type(trainX) == list
assert type(trainY) == list
assert type(testX) == list
assert type(testY) == list
assert len(trainX) == len(trainY)
assert len(testX) == len(testY)
assert len(trainX) == len(trainY)
assert len(testX) == len(testY)
assert len(trainX) == len(trainY)
assert len(testX) == len(testY)
assert len(trainX) == len(trainY)
assert len(testX) == len(testY)
assert len(trainX) == len(trainY)
assert len(testX) == len(testY)
assert len(trainX) == len(trainY)
assert len(testX) == len(testY)
assert len(trainX) == len(trainY)
assert len(testX) == len(testY)
assert len(trainX) == len(trainY)
assert len(testX) == len(testY)
assert len(trainX) == len(trainY)
assert len(testX) == len(testY)
assert len(trainX) == len(trainY)
assert len(testX) == len(testY)
assert len(trainX) == len(trainY)
assert len(testX) == len(testY)
assert len(trainX) == len(trainY)
assert len(testX) == len(testY)
assert len(trainX) == len(trainY)
assert len(testX) == len(testY)
assert len(trainX) == len(trainY)
assert len(testX) == len(testY)
assert len(trainX) == len(trainY)
assert len(testX) == len(testY)
assert len(trainX) == len(trainY)
assert len(testX) == len(testY)
assert len(trainX)
### END SOLUTION
b = gridsearch.score(trainX, trainY)
c = gridsearch.predict(trainX)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump((b, c), f)
