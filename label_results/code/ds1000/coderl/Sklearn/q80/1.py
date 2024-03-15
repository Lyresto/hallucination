import numpy as np

def kmeans(df):
	n = len(df)
	# get columns of df
	cols = df.columns.values
	# transform to numpy array
	df = np.array(df[cols])
	# KMEANS
	kmeans = KMeans(n_clusters=2).fit(df)
	labels = kmeans.predict(df)
	# Centroid values
	centroids = kmeans.cluster_centers_
	#print(centroids)
	return labels, centroids
