import numpy as np

def vec2matrix(arr, ncol):
	return np.mat(arr).T.tolist()
