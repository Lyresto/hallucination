X = df['mse'].values.reshape(-1, 1)
kmeans = KMeans(n_clusters=2).fit(X)
labels = kmeans.predict(X)
