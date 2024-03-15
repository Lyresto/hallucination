import scipy.spatial
import numpy as np

def closest_point_to_cluster(centroids, data):
	return [np.argmin(np.sum(data, axis=centroids[i,:] - centroids[i,:]) / (len(centroids) - i)).tolist() for i in range(len(centroids))]
