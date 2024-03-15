To extract the closest point to each cluster's centroid, you can use the following code:

```python
import numpy as np
from scipy.spatial.distance import cdist
from scipy.cluster.hierarchy import linkage, cut_tree

# Generate random data
centroids = np.random.rand(5, 3)
data = np.random.rand(100, 3)

# Compute the pairwise distances between data points and centroids
distances = cdist(data, centroids)

# Perform hierarchical clustering
Z = linkage(distances, method='single')

# Assign samples to clusters
labels = cut_tree(Z, n_clusters=5).flatten()

# Find the closest point to each cluster's centroid
result = np.zeros((5, 3))
for i in range(5):
    cluster_points = data[labels == i]
    centroid = centroids[i]
    closest_point = cluster_points[np.argmin(cdist(cluster_points, [centroid]))]
    result[i] = closest_point

print(result)
```

This code first computes the pairwise distances between the data points and the centroids using `cdist` from `scipy.spatial.distance`. Then, it performs hierarchical clustering using `linkage` from `scipy.cluster.hierarchy` and assigns each sample to a cluster using `cut_tree`. Finally, it iterates over each cluster, finds the closest point to the centroid using `np.argmin` and `cdist`, and stores it in the `result` array.