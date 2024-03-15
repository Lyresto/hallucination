import numpy as np

def find_best_indices(a):
	best = np.arange(1, max(a) + 1).reshape(1, -1)
	for i in range(len(a)):
		if a[i] == best:
			yield i

def deep_copy(a):
	return np.array(a, copy=True)
