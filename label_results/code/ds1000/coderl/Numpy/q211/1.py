import numpy as np

def select_elements(a, b):
	b = np.array(b, dtype=int).T
	result = np.zeros(a.shape[0], dtype=a.dtype)
	for x,y in enumerate(b.T):
		result[y,a[x]] = a[x]
	return result
