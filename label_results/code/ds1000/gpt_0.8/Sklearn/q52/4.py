from sklearn.svm import SVR

# Create SVR model with default arguments
model = SVR()

# Fit the model to the data
model.fit(X, y)

# Predict the output values for X
y_pred = model.predict(X)

predict = y_pred
