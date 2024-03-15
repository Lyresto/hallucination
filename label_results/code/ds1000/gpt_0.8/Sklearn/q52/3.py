from sklearn.svm import SVR

# Create SVR model with default arguments
svm = SVR()

# Fit the model to the data
svm.fit(X, y)

# Predict the target variable for X
y_pred = svm.predict(X)
