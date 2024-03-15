import numpy as np
import sklearn

def select_features(features):
	y = np.zeros((len(features), len(features[0])), dtype=int)
	for i, x in enumerate(zip(*features)):
		y[i] = 1
	return np.array(y)
