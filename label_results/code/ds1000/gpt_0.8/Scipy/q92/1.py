One way to find the closest element to each cluster's centroid is to calculate the pairwise distances between the centroids and the original data points, and then find the index of the minimum distance for each cluster.

Here's the code to achieve that:

```python
import numpy as np
from scipy.spatial.distance import cdist

# Calculate pairwise distances between centroids and data points
distances = cdist(centroids, data)

# Find the index of the closest data point for each cluster
closest_indices = np.argmin(distances, axis=1)

result = closest_indices
```

Now `result` will contain the index of the closest element in the original data for each cluster.