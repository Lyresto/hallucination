model = xgb.XGBRegressor()
paramGrid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [3, 4, 5],
    'learning_rate': [0.1, 0.01, 0.001]
}
fit_params={"early_stopping_rounds":42,
            "eval_metric" : "mae",
            "eval_set" : [(testX, testY)]}

gridsearch = GridSearchCV(estimator=model, param_grid=paramGrid, cv=TimeSeriesSplit(n_splits=3).get_n_splits([trainX, trainY]), n_jobs=-1)
gridsearch.fit(trainX, trainY, **fit_params)

# Get the best parameters and score
best_params = gridsearch.best_params_
best_score = gridsearch.best_score_

# Fit the model with the best parameters
best_model = xgb.XGBRegressor(**best_params)
best_model.fit(trainX, trainY, **fit_params)

# Get the predictions
predictions = best_model.predict(testX)
