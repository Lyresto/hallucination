from sklearn.svm import SVR

# Initialize SVR model with default arguments
regressor = SVR()

# Fit the model to the data
regressor.fit(X, y)

# Predict the target variable
predict = regressor.predict(X)
