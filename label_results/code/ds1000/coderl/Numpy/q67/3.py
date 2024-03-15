import numpy as np

def sort_matrices(a, axis=None):
	b = np.sort(a, axis)
	if axis is None:
		return list(zip(*b))
	else:
		return list(zip(*b)[axis])
