import numpy as np
def solve(a, b):
	c = np.zeros(a.shape[0]*a.shape[1], dtype=np.int)
	for n,i in enumerate(b):
		c[i] = a[n][i]
	return c.astype(np.int)
