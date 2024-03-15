To find the closest point to each cluster centroid, you can use the following code:

```python
import numpy as np
import scipy.spatial

centroids = np.random.rand(5, 3)
data = np.random.rand(100, 3)

# Calculate the distance between each data point and each centroid
distances = scipy.spatial.distance.cdist(data, centroids)

# Find the index of the closest centroid for each data point
closest_centroids = np.argmin(distances, axis=1)

# Find the closest point to each centroid
result = np.zeros(centroids.shape)
for i in range(centroids.shape[0]):
    cluster_points = data[closest_centroids == i]
    closest_point = cluster_points[np.argmin(scipy.spatial.distance.cdist(cluster_points, [centroids[i]]))]
    result[i] = closest_point
```

This code uses the `cdist` function from scipy.spatial.distance to calculate the pairwise distances between each data point and each centroid. Then, it finds the index of the closest centroid for each data point using `argmin`. Finally, it loops over each cluster, selects the data points belonging to that cluster, and finds the closest point to the centroid using `cdist` and `argmin` again.

The result variable will be a numpy array containing the closest point to each cluster centroid.