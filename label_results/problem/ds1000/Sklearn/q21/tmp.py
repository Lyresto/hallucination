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
# Define the XGBoost model
model = xgb.XGBRegressor()

# Define the parameter grid to search
param_grid = {
    'max_depth': [3, 4, 5],
    'learning_rate': [0.1, 0.01, 0.001],
    'n_estimators': [100, 500, 1000]
}

# Define the fit parameters for early stopping
fit_params = {
    'early_stopping_rounds': 10,
    'eval_metric': 'mae',
    'eval_set': [(testX, testY)]
}

# Perform grid search with early stopping
gridsearch = GridSearchCV(model, param_grid, cv=TimeSeriesSplit(n_splits=3).get_n_splits([trainX, trainY]), 
                          n_jobs=-1, verbose=1, fit_params=fit_params)
gridsearch.fit(trainX, trainY)

# Get the best hyperparameters and score
best_params = gridsearch.best_params_
b = gridsearch.best_score_

# Make predictions with the best model
best_model = xgb.XGBRegressor(**best_params)
best_model.fit(trainX, trainY, early_stopping_rounds=10, eval_metric='mae', eval_set=[(testX, testY)])
c = best_model.predict(testX)

### END SOLUTION
b = gridsearch.score(trainX, trainY)
c = gridsearch.predict(trainX)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump((b, c), f)
