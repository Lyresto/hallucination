import scipy.spatial
import numpy as np

def closest_point(centroids, data):
	result = np.array([])
	for i in range(len(centroids)):
		result = np.append(result, [np.min(scipy.spatial.distance.cdist(data,centroids[i]).item())])
	return result
