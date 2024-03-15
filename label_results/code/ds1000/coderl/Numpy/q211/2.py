import numpy as np
def select_elements(a, b):
	c = np.empty(len(a), dtype = int)
	for i, j in enumerate(b):
		c[i] = a[b[i][0]].index(a[b[i][1]])
	return c
