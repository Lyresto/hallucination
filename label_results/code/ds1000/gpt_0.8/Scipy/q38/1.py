To calculate the pairwise Euclidean distances between all regions in the raster, you can use the `cdist` function from the `scipy.spatial.distance` module. However, since `cdist` expects a 1D array as input, you will need to reshape your 2D array into a 1D array. Here's how you can do it:

```python
import numpy as np
from scipy.spatial.distance import cdist

# Reshape the 2D array into a 1D array
reshaped_array = example_array.reshape(-1)

# Calculate the pairwise Euclidean distances using cdist
distances = cdist(np.argwhere(reshaped_array > 0), np.argwhere(reshaped_array > 0))

# Convert the distances from cells to meters by multiplying with the raster resolution
# Assuming the raster resolution is 1 (change this value accordingly)
distances *= 1

# Convert the distances to a N*N array in the form of "from ID, to ID, distance"
n = reshaped_array.max()  # Number of unique IDs
result = np.zeros((n, n, 3))
for i in range(n):
    for j in range(n):
        result[i, j, 0] = i + 1  # From ID
        result[i, j, 1] = j + 1  # To ID
        result[i, j, 2] = distances[i, j]  # Distance

# Print the result
print(result)
```

This will give you a N*N array `result` containing the minimum distances separating the nearest edges of each raster patch, in the form of "from ID, to ID, distance".