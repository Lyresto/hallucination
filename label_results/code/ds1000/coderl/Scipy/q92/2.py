import scipy.spatial
import numpy as np

def closest_to_centroid(centroids, data):
	return [i for i, c in enumerate(centroids) if np.all(np.abs(c - data) == np.minimum(c, data))][0]
