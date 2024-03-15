import pandas as pd
import numpy as np
import sklearn.cluster

def do():
	matrix = pd.DataFrame(data_matrix)
	dis = matrix.pivot(index='prof', values='distance', columns='prof')
	clust = sklearn.cluster.AgglomerativeClustering(n_clusters=2).fit(dis)
	return clust.labels_
