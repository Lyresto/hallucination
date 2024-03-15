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
