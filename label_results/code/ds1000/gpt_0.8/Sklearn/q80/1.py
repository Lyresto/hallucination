import numpy as np

mse_values = df['mse'].values
X = np.array(mse_values).reshape(-1, 1)

kmeans = KMeans(n_clusters=2).fit(X)
labels = kmeans.labels_
END SOLUTION
