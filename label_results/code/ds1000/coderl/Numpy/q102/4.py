import numpy as np

def extract_columns(a, low, high):
	for i in range(low, high + 1):
		a[:] = np.take(a, range(1, i + 1), axis=0)
	return a
