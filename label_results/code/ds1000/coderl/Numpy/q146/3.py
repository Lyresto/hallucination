import numpy as np

def mask(a):
	min_value = np.min(a, axis=1)
	return np.array([[value is min_value for value in arr] for arr in a])
