kmeans = KMeans(n_clusters=2).fit(df)
labels = kmeans.predict(df)
