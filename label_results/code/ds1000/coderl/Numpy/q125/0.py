import numpy as np
def mean(arr, size):
	return np.mean(np.array(arr).reshape(-1, size)).tolist()
