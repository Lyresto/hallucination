import numpy as np

def distance_matrix(a):
	m, n = len(a), len(a[0])
	dist = np.zeros((m, n), dtype=np.int)
	for i in range(m):
		for j in range(n):
			dist[i, j] = np.abs(a[i][j] - a[i][j-1])
	return dist
