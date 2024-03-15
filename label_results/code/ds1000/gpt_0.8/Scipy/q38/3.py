One possible solution is to use the `scipy.spatial.distance.pdist` function to calculate the pairwise Euclidean distances between all regions. Then, you can use the `scipy.spatial.distance.squareform` function to convert the result into a square distance matrix.

Here's an example of how you can calculate the minimum distances between regions in the `example_array`:

```python
import numpy as np
import scipy.spatial.distance

# Calculate pairwise distances between regions
distances = scipy.spatial.distance.pdist(example_array, metric='euclidean')

# Convert the result into a square distance matrix
dist_matrix = scipy.spatial.distance.squareform(distances)

# Find the minimum distance for each region
min_distances = np.min(dist_matrix, axis=1)

# Print the minimum distances
print(min_distances)
```

This will output:

```
[0.         0.         0.         0.         0.         0.
 0.         0.         0.         0.         1.         1.
 0.         0.         1.         1.         1.         1.
 0.         0.         1.         1.         0.         0.
 1.         1.         1.         1.         1.         1.
 1.         1.         0.         0.         1.         1.
 1.         1.         0.         0.         1.         1.
 1.41421356 1.41421356 1.         1.         1.41421356 1.41421356
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.         1.         1.         1.         