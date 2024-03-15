import scipy.spatial
def dist(a, b):
	return np.minimum(scipy.spatial.distance.cdist(a, b), scipy.spatial.distance.cdist(b, a)).round()
