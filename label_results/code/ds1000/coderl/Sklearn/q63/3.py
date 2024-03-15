import pandas as pd
import numpy as np
import sklearn.cluster

def distance(x,y):
	return np.sqrt((x-y)**2)

def normalize(matrix):
	matrix = matrix - matrix.min()
	matrix = matrix / matrix.max()
	matrix = matrix.T
	return matrix

def agglomerative_clustering(matrix):
	clusterer = sklearn.cluster.AgglomerativeClustering(n_clusters=2)
	clusterer.fit(normalize(matrix))
	label = clusterer.labels_
	return [str(i) for i in range(2)]
