import numpy as np

def sort_matrices(a, b):
	import numpy.argsort
	return np.sort(b, axis=0).tolist()
