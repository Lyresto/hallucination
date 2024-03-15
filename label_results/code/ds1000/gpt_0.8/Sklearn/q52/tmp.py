import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
import sklearn

X, y = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create a support vector regression model with a Gaussian kernel
regressor = SVR(kernel='rbf')

# Fit the model to the training data
regressor.fit(X_train, y_train)

# Predict the target variable for the test data
y_pred = regressor.predict(X_test)



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(predict, f)
