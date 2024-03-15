import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold

def proba(X, y):
	logreg = LogisticRegression()
	cv = StratifiedKFold(5).split(X, y)
	proba = []
	for train, test in cv:
		logreg.fit(X[train], y[train])
		p = logreg.predict_proba(X[test])
		proba.append(p[0])
	return proba

def load_data():
	X = np.loadtxt('X.txt')
	y = np.loadtxt('y.txt')[:, 0]
	return X, y
