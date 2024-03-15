import numpy as np

def vec2matrix(arr, ncol):
	return np.dot(arr, np.expand_dims(arr, axis=1))
