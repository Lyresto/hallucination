One way to solve this problem is to iterate over each cluster, calculate the distance between each element in the cluster and the centroid of the cluster, and then select the element with the minimum distance.

Here's one possible solution:

```python
import numpy as np
from scipy.spatial import distance

centroids = np.random.rand(5, 3)
data = np.random.rand(100, 3)

result = []

# Iterate over each cluster
for i in range(len(centroids)):
    cluster_indices = np.where(clusters == i)[0]  # Get the indices of elements in the current cluster
    cluster_data = data[cluster_indices]  # Get the data points in the current cluster
    cluster_centroid = centroids[i]  # Get the centroid of the current cluster
    
    # Calculate the distance between each element in the cluster and the centroid
    distances = distance.cdist(cluster_data, [cluster_centroid])
    
    # Find the index of the element with the minimum distance
    closest_index = np.argmin(distances)
    
    # Add the closest element to the result
    result.append(cluster_data[closest_index])

result = np.array(result)
```

The `result` variable will then contain the closest element to each cluster's centroid.