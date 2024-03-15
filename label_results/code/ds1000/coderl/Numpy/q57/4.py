import numpy as np

def get_max_sets(a):
	N = len(a)
	V = [[] for _ in range(N)]
	for i, j in enumerate(a):
		for k in range(len(j)):
			V[i].append(np.argwhere(j == k)[0][0])
	V.sort()
	return V[0]
