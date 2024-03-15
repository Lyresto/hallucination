# Solution
To find the closest point to each cluster centroid, we can iterate over each cluster, calculate the distances between all points in the cluster and the centroid, and select the point with the minimum distance.

Here's one way to implement this:

```python
import numpy as np
from scipy.spatial import distance

# Example data
centroids = np.random.rand(5, 3)
data = np.random.rand(100, 3)

result = []
for centroid in centroids:
    cluster_points = data[np.argmin(distance.cdist(data, [centroid]), axis=0)]
    result.append(cluster_points)

result = np.array(result)
```

The `distance.cdist` function calculates the pairwise distances between `data` and `centroid`. `np.argmin` is used to find the index of the point with the minimum distance for each column (i.e., each point in `data`). Finally, we append the selected points to the `result` list.

Note that the result will be a 2D array with shape `(n_clusters, 3)`, where `n_clusters` is the number of clusters.

Hope this helps!