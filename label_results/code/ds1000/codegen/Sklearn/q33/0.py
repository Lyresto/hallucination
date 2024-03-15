
regressor = RandomForestRegressor(n_estimators=150, min_samples_split=1.0, random_state=42)
rgr = regressor.fit(X,y)
predict = rgr.predict(X_test)
