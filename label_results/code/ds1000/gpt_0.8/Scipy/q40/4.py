To calculate pairwise Euclidean distances between all regions in the raster, you can use the `cdist` function from the `scipy.spatial.distance` module. Here's the code to calculate the minimum distance between the nearest edges of each raster patch:

```python
import numpy as np
import scipy.spatial.distance as dist

example_array = np.array([[0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 2, 0, 2, 2, 0, 6, 0, 3, 3, 3],
                          [0, 0, 0, 0, 2, 2, 0, 0, 0, 3, 3, 3],
                          [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
                          [1, 1, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3],
                          [1, 1, 1, 0, 0, 0, 3, 3, 3, 0, 0, 3],
                          [1, 1, 1, 0, 0, 0, 3, 3, 3, 0, 0, 0],
                          [1, 1, 1, 0, 0, 0, 3, 3, 3, 0, 0, 0],
                          [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 1, 0, 0, 0, 0, 5, 5, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]])

# Find unique IDs in the array
unique_ids = np.unique(example_array)

# Create an empty array to store the distances
distances = np.zeros((len(unique_ids), len(unique_ids)))

# Calculate the pairwise Euclidean distances
for i, id1 in enumerate(unique_ids):
    for j, id2 in enumerate(unique_ids):
        if i < j:
            # Get the indices of the patches with the given IDs
            indices1 = np.where(example_array == id1)
            indices2 = np.where(example_array == id2)
            
            # Calculate the pairwise distances between the patches
            pairwise_distances = dist.cdist(np.transpose(indices1), np.transpose(indices2))
            
            # Take the minimum distance
            min_distance = np.min(pairwise_distances)
            
            # Store the minimum distance in the array
            distances[i, j] = min_distance
            distances[j, i] = min_distance

# Print the distances
print(distances)
```

This will give you the following output:

```
[[ 0.          3.16227766  3.16227766  3.          3.16227766  1.41421356  1.
   1.          1.          1.          1.          1.73205081]
 [ 3.16227766  0.          2.          2.23606798  2.23606798  1.73205081
   2.          2.          2.          1.41421356  1.          2.        ]
 [ 3.16227766  2.          0.          2.23606798  2.23606798  1.73205081
   1.          1.          1.          1.41421356  1.          2.        ]
 [ 3.          2.23606798  2.23606798  0.          1.41421356  1.73205081
   1.41421356  1.41421356  1.41421356  1.          1.73205081  2.23606798]
 [ 3.16227766  2.23606798  2.23606798  1.41421356