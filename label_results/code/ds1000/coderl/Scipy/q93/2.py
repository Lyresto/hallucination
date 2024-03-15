import scipy.spatial
import numpy as np

def closest_point_to_centroid(centroids, data):
	return list(map(lambda x: np.mean(x), np.percentile(data, 100)))
