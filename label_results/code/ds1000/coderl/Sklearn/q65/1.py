def hierarchical_clustering(simM):
	labels = sklearn.cluster.AgglomerativeClustering(n_clusters=2).fit_predict(simM)
	return [labels.index(i) for i in range(len(labels))]
