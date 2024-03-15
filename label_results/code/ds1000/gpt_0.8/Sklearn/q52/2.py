from sklearn.svm import SVR

# Create the SVR model with default arguments
model = SVR(kernel='rbf')

# Fit the model to the training data
model.fit(X, y)

# Predict the target variable for X
predict = model.predict(X)
