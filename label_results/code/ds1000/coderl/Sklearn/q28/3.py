import numpy as np
from sklearn.svm import LinearSVC

def cross_val_score(model, X, y, cv=5):
	# your code
	scores = np.zeros(cv)
	for i in range(len(X)):
		scores[i] = model.score(X[i], y[i])
	return f'Name model: {model}, Mean score: {scores.mean()}'
