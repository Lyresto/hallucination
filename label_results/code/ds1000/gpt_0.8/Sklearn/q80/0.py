f1 = df['mse'].values.reshape(-1, 1)
kmeans = KMeans(n_clusters=2).fit(f1)
labels = kmeans.labels_
