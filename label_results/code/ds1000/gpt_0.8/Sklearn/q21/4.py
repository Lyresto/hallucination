model = xgb.XGBRegressor()
paramGrid = {
    "max_depth": [3, 5, 7],
    "learning_rate": [0.1, 0.01, 0.001],
    "n_estimators": [100, 500, 1000]
}

fit_params = {
    "early_stopping_rounds": 42,
    "eval_metric": "mae",
    "eval_set": [(testX, testY)]
}

gridsearch = GridSearchCV(model, paramGrid, verbose=1, cv=TimeSeriesSplit(n_splits=3).get_n_splits([trainX, trainY]), n_jobs=-1, iid=False)

gridsearch.fit(trainX, trainY, **fit_params)

b = gridsearch.best_score_
c = gridsearch.predict(testX)
