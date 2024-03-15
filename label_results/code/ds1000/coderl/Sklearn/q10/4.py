import numpy as np
import pandas as pd
from sklearn import svm

def proba(X, y, x_predict):
	predicted = model.predict(x_predict)
	decision_function = model.decision_function(x_predict)
	return 1 / (1 + np.exp(-predicted))

def predict(X, y):
	return np.where(y == X[:, 0], 1, 0)


def score(X, y):
	return np.where(y == X[:, 0], X[:, 1] - y * (X[:, 1] > 0), 0, 1)

def load_data():
	X = np.array([[i, i] for i in range(len(X))])
	y = np.array([i for i in range(len(X))])
	x_predict = np.array([i for i in range(len(X))])
	return X, y, x_predict
