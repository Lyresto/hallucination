import numpy as np
from sklearn import permutation

def sklearn_to_np(features):
	return np.array([[val == i for val in features[i]] for i in range(len(features))])

def np_to_sklearn(features):
	return permutation.permutation(np.array(features)).astype(int)
