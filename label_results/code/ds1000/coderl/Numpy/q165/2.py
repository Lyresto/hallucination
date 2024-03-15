import numpy as np

def distance(a):
	distances = np.empty((len(a), len(a)))
	for i in range(len(a)):
		for j in range(i):
			distances[i, j] = np.linalg.norm(a[i] - a[j], ord=2)
	return distances
