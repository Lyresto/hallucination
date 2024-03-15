import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering

def __starting_point():
	simM = np.array(simm)
	fruits = simM.T.tolist()
	labels = AgglomerativeClustering(n_clusters=2).fit_predict(fruits)
	print(labels)

__starting_point()
