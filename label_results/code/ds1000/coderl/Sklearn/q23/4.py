import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold

def proba(X, Y):
	scores = []
	for train, test in cv.split(X, Y):
		lr = LogisticRegression()
		lr.fit(X[train], Y[train])
		scores.append(lr.score(X[test], Y[test]))
	return scores

def load_data():
	X = np.array(pd.read_csv('experiments/logistic_regression.csv'))[:, :2]
	Y = np.array(pd.read_csv('experiments/logistic_regression.csv')[:, :2])[:, 1]
	return X, Y
