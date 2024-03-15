import pandas as pd
from scipy.spatial import distance
import numpy as np

def load_data():
	matrix = np.array(pd.DataFrame(data=np.array(data_matrix)).T)
	return sklearn.cluster.AgglomerativeClustering(n_clusters=2).fit(matrix).labels_
