import numpy as np

def shift(arr, shift):
	m, n = shift[0], shift[1]
	return np.rot90(np.array(arr))[m:n+m, m:n+n]
