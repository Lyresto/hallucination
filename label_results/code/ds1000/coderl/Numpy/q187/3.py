import numpy as np

def solve(a):
	return np.dot(a, np.dot(a.T, a))
