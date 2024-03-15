from scipy.cluster.hierarchy import linkage

def closest_to_centroid(centroids, data):
	return list(map(linkage(lambda i,j: tuple(i), data, centroid, mode='distance')[0][0]))
