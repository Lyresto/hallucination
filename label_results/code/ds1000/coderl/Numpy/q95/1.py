import numpy as np


def sliding_window(a):
	n, m = len(a), len(a[0])
	patch = np.zeros((n, n//2 + 1), dtype=np.int)
	for i in range(n):
		for j in range(m):
			x, y = i*2, j*2
			patch[x:y, x:y] += a[i][j]
	return patch
