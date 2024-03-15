import sklearn.cluster
import numpy as np

def distance_matrix(matrix):
	return np.array(matrix).astype(float)

def compute_label(matrix):
	labels = [0 for _ in range(len(matrix))]
	for i, row in enumerate(matrix):
		for j in range(len(row)):
			labels[row[j]] = i + 1
	return labels

def find_cluster(matrix):
	label = sklearn.cluster.AgglomerativeClustering(n_clusters=2).fit(distance_matrix(matrix))
	return label.labels_
	
def load_data():
	matrix = np.array(pd.read_csv('data/matrix.csv'))
	return find_cluster(matrix)
