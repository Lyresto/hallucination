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
import xgboost as xgb
from sklearn.model_selection import cross_val_predict





def score(model, x, y):
    return model.score(x, y)





def grid_search(gs, trainX, trainY, testX, testY):
    param_grid = dict(list(zip(trainX, trainY)))
    gs.fit(trainX, trainY, **param_grid)
    b = [score(gs, x, y) for x, y in zip(testX, testY)]
    c = [cross_val_predict(gs, x, y) for x, y in zip(testX, testY)]
    return b, c





def load_data():
    b, c = grid_search(xgb.XGBRegressor(), trainX, trainY, testX, testY)
    return b, c



### END SOLUTION
b = gridsearch.score(trainX, trainY)
c = gridsearch.predict(trainX)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump((b, c), f)
