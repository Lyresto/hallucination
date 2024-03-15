import numpy as np
from sklearn import datasets

# from sklearn.datasets import load_iris
# X = iris.data[(iris.target==0) | (iris.target==1)]
# Y = iris.target[(iris.target==0) | (iris.target==1)]

# Divide data into 80% training, 20% testing.
# Class 0 has indices 0-49. Class 1 has indices 50-99.
# Initializing the GBR to 1.

# X_train = [[0]*40 + [1]*40]
# y_train = [0, 0, 1, 1]
# X_test = [[0]*40 + [1]*40]
# y_test = [0, 0, 1, 1]

# Initialize the GBR.
GBR = GradientBoostingClassifier(n_estimators=50,max_depth=8)

# Fit the GBR.
GBR.fit(np.array(X_train), np.array(y_train))

# Predict the test set results.
Y_pred = GBR.predict(np.array(X_test))

# Print the result.
print(Y_pred)





#BEGIN SOLUTION
