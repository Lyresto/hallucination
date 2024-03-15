f1 = df['mse'].values.reshape(-1, 1)
kmeans = KMeans(n_clusters=2).fit(f1)
labels = kmeans.predict(f1)
centroids = kmeans.cluster_centers_
