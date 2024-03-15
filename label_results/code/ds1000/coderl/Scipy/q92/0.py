import scipy.spatial
import numpy as np
import itertools

def closest_to_centroid(data, centroids):
	return list(itertools.accumulate(np.searchsorted(centroids, x) for x in data))[0]
