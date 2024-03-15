import numpy as np
f1 = df['mse'].values
f1 = f1.reshape(-1, 1)
kmeans = KMeans(n_clusters=2).fit(f1)
labels = kmeans.predict(f1)
