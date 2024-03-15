import numpy as np

# Reshape the mse values to a 2D array
mse_values = df['mse'].values.reshape(-1, 1)

# Use KMeans clustering on mse values
kmeans = KMeans(n_clusters=2).fit(mse_values)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_
