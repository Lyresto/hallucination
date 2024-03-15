You can use the `cdist` function from the `scipy.spatial.distance` module to calculate the pairwise distances between all points in the input data.

Here is an example of how you can use it to calculate the distances between each point in `a` and all other points:

```python
import numpy as np
from scipy.spatial.distance import cdist

a = np.array([[1,2,8],
              [7,4,2],
              [9,1,7],
              [0,1,5],
              [6,4,3]])

distances = cdist(a, a)
```

The `cdist` function returns a 2D array where the element at index `(i, j)` represents the distance between the `i`-th point and the `j`-th point. The resulting array is symmetric, so the distance between point `i` and point `j` is the same as the distance between point `j` and point `i`.

You can then access the distances for a specific point by indexing the `distances` array. For example, to get the distances of the first point `[1, 2, 8]` from all other points, you can use `distances[0]`.

Note that the `cdist` function supports various distance metrics, so you can specify a different metric if needed. By default, it uses the Euclidean distance.

I hope this helps! Let me know if you have any further questions.