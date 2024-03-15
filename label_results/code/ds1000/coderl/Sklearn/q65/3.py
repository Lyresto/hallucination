import pandas as pd
import numpy as np
import sklearn.cluster

def agglomerative_clustering(simM):
	fruits = simM.index.values
	cluster_labels = [0]*len(fruits)
	distance_matrix = np.array(simM)
	fruit_list = []
	for i, fruit in enumerate(fruits):
		fruit_list.append(i)
	for row in distance_matrix:
		col = np.argwhere(row == row.min())
		fruit_idx = col[0][0]
		distance_matrix[fruit_idx, col] = 1
	clus = sklearn.cluster.AgglomerativeClustering(n_clusters=2)
	clus.fit(distance_matrix)
	return cluster_labels
