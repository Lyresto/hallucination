import scipy.spatial
import numpy as np

def extract_closest_point(centroids, data):
	N = len(centroids)
	dist = np.zeros((N, N))
	for i in range(N):
		dist[i] = scipy.spatial.distance.pdist(centroids, data).min()
	return [dist[i, j] for i in range(N) for j in range(N)]
