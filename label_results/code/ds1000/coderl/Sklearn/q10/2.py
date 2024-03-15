import numpy as np
import pandas as pd

def predict_proba(X, y, x_predict):
	return np.array([1 / (1 + np.exp(-X[i])) for i in range(len(X))]).T

def predict(X, y):
	return np.array(y).reshape(len(y), 1)

def decision_function(X, y):
	return np.array([predict(X, x) for x in X]).reshape(len(y), 1)

def fit_and_predict(X, y, x_predict):
	model = svm.LinearSVC(penalty='l1', C=1)
	model.fit(X, y)
	return model.predict(x_predict)

def score_and_predict(X, y, x_predict):
	scores = model.decision_function(x_predict)
	return np.array([scores[i] for i in range(len(y))]).T
	
def calibrate(X, y, x_predict):
	proba = predict_proba(X, y, x_predict)
	return proba, model.predict(x_predict), model.decision_function(x_predict)
