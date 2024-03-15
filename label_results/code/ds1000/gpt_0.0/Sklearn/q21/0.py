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
