import numpy as np
import pandas as pd
import sklearn.cluster

def label(matrix, fruit):
	dist = np.sqrt(np.sum(np.square(matrix), axis=1))
	res = sklearn.cluster.AgglomerativeClustering(n_clusters=2).fit_predict(dist)
	return [i for i, c in enumerate(res) if c == fruit][0]


def load_data():
	simM = np.array(pd.read_csv('simulation.csv').values)
	return label(simM, 'fruit1')
