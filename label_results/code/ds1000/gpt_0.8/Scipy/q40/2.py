To calculate the pairwise Euclidean distances between all regions in the raster, you can use the `cdist` function from the `scipy.spatial.distance` module. Here's the solution code:

```python
import numpy as np
from scipy.spatial.distance import cdist

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

# Get the unique IDs of the regions
unique_ids = np.unique(example_array)

# Initialize an empty array to store the pairwise distances
distances = np.zeros((len(unique_ids), len(unique_ids)))

# Loop over each pair of unique IDs and calculate the Euclidean distance
for i, id1 in enumerate(unique_ids):
    for j, id2 in enumerate(unique_ids):
        patch1 = np.where(example_array == id1)
        patch2 = np.where(example_array == id2)
        distance = np.min(cdist(patch1, patch2))
        distances[i, j] = distance

# Print the distances
for i, id1 in enumerate(unique_ids):
    for j, id2 in enumerate(unique_ids):
        print(f"From ID {id1} to ID {id2}: {distances[i, j]}")
```

This code will calculate the minimum distance between the nearest edges of each pair of regions and print the results. Note that the `cdist` function requires the input arrays to have the same number of columns, so we use `np.where` to find the indices of the cells with the same ID for each region.