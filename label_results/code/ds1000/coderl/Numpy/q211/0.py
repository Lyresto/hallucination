import numpy as np
def select_elements(a, b):
	N, M = a.shape
	target = np.zeros((N, M), dtype=np.int)
	for n, i in enumerate(b):
		target[n, i] = np.argwhere(a == i)[0].tolist()
	return target
