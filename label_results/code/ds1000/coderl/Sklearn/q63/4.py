from sklearn.cluster import AgglomerativeClustering
from scipy.spatial.distance import pdist
from itertools import product

def load_data():
	return [[k, v] for k, v in zip(*zip(*np.sort(pdist(pd.DataFrame(data).T).T))[::2])]

def label(matrix):
	clus = AgglomerativeClustering(n_clusters=2).fit(distance_matrix)
	return [c for c in clus.labels_ if c!= 0].pop()
