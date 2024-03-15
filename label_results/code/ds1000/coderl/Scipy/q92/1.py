import numpy as np
import scipy.spatial
import pandas as pd

def distance_matrix(centroids, data):
	distances = np.sqrt(np.sum(np.square(data - centroid) for centroid in centroids))
	return distances

def closest_element(data, clusters, index):
	return list(filter(lambda x: x[0] == index, clusters))[0][1]

def solve(data, clusters, result):
	distances = distance_matrix(data, data)
	clusts = np.expand_dims(distances, axis=0)
	cluster_tree = scipy.cluster.hierarchy.cut_tree(clusts, distance=distances)
	closest = [None]*len(clusters)
	for i, cluster in enumerate(cluster_tree):
		closest[i] = closest_element(data, cluster, i)
	return closest
