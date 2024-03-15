To calculate pairwise Euclidean distances between all regions in the raster, we can use the `cdist` function from the `scipy.spatial.distance` module. Here's how you can solve this problem:

```python
import numpy as np
from scipy.spatial.distance import cdist

def calculate_distances(example_array):
    # Get the unique IDs in the array
    unique_ids = np.unique(example_array)

    # Get the coordinates of each unique ID in the array
    coordinates = []
    for unique_id in unique_ids:
        coordinates.append(np.argwhere(example_array == unique_id))

    # Calculate pairwise Euclidean distances between coordinates
    distances = cdist(np.concatenate(coordinates), np.concatenate(coordinates))

    # Create an array to store the distances between regions
    region_distances = np.zeros((len(unique_ids), len(unique_ids)))

    # Fill the array with the minimum distances between regions
    for i in range(len(unique_ids)):
        for j in range(len(unique_ids)):
            if i != j:
                region_distances[i, j] = np.min(distances[i * len(coordinates[i]): (i + 1) * len(coordinates[i]),
                                                  j * len(coordinates[j]): (j + 1) * len(coordinates[j])])

    return region_distances

# Test the function with the example array
result = calculate_distances(example_arr)
print(result)
```

The function `calculate_distances` takes the example array as input and returns an array `region_distances` containing the minimum distances between regions. Each element `region_distances[i, j]` represents the minimum distance between region `i` and region `j`.

Note: The code assumes that the regions in the array are represented by unique integer IDs. If the regions are represented by other data types, you may need to modify the code accordingly.