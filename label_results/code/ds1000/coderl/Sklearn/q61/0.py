import numpy as np

def solve(features):
	X = np.zeros((len(features), len(features[0])), dtype=object)
	for i in range(len(X)):
		for j in range(len(features[i])):
			X[i, features[i][j]] = 1
	return X
