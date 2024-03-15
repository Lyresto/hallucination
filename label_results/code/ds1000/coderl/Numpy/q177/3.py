import numpy as np

def sliding_window(a, size):
	n, m = size
	return [np.zeros((i, n+i)) for i in range(n)]
