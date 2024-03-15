import numpy as np

def extrema(n, arr):
	c, s = np.modf(np.abs(arr))
	return [i for i in range(len(arr)) if c <= n and s < n][::-1]
