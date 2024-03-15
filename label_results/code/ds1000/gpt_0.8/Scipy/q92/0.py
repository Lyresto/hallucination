One way to solve this problem is to calculate the distance between each data point and the centroids, and then find the closest point to each centroid. Here's one possible solution:

```python
import numpy as np
from scipy.spatial.distance import cdist

# Calculate the distance between each data point and each centroid
distances = cdist(data, centroids)

# Find the index of the closest data point for each centroid
closest_indices = np.argmin(distances, axis=0)

result = closest_indices
```

In this solution, `cdist` calculates the distances between each data point in `data` and each centroid in `centroids`. The `argmin` function is then used to find the index of the data point that has the smallest distance for each centroid. The resulting indices are stored in the `result` variable.