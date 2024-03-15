import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering

def __starting_point():
	simM = pd.DataFrame(simM)
	clusters = AgglomerativeClustering(n_clusters=2).fit(simM)
	cluster_labels = clusters.labels_
	print(cluster_labels)
__starting_point()
