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
model = xgb.XGBRegressor()
paramGrid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [3, 4, 5],
    'learning_rate': [0.01, 0.1, 1.0]
}
fit_params = {
    "early_stopping_rounds": 42,
    "eval_metric": "mae",
    "eval_set": [[testX, testY]]
}
gridsearch = GridSearchCV(model, paramGrid, verbose=1, cv=TimeSeriesSplit(n_splits=3).get_n_splits([trainX, trainY]), n_jobs=n_jobs, iid=iid)
gridsearch.fit(trainX, trainY, **fit_params)
b = gridsearch.best_score_
c = gridsearch.predict(testX)



### END SOLUTION
b = gridsearch.score(trainX, trainY)
c = gridsearch.predict(trainX)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump((b, c), f)
