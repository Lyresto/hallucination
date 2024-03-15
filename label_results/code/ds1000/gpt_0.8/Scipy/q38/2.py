To calculate pairwise Euclidean distances between all regions in a raster, we can use the `cdist` function from the `scipy.spatial.distance` module. However, since the raster has a unique ID for each patch/region, we need to convert it into a binary matrix where each patch/region is represented by a separate binary value.

Here's the code to calculate pairwise Euclidean distances between all regions in the raster:

```python
import numpy as np
from scipy.spatial.distance import cdist

# Convert raster into binary matrix
unique_values = np.unique(example_array)
binary_matrix = np.zeros_like(example_array, dtype=int)
for i, value in enumerate(unique_values):
    binary_matrix[example_array == value] = i+1

# Calculate pairwise Euclidean distances
distances = cdist(binary_matrix.flatten()[:, np.newaxis], binary_matrix.flatten()[:, np.newaxis], metric='euclidean')

# Create N*N array with distances between all possible combinations of regions
n = len(unique_values)
result = np.zeros((n**2, 3), dtype=int)
for i in range(n):
    for j in range(n):
        result[i*n+j] = [i+1, j+1, distances[i, j]]

print(result)
```

This will give you a N*N array in the form of "from ID, to ID, distance", including distances between all possible combinations of regions. Note that we use `binary_matrix.flatten()[:, np.newaxis]` to convert the flattened binary matrix into a column vector before passing it to `cdist`.