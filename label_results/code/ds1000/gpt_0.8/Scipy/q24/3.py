# Approach:
To solve this problem, we can use the Hungarian algorithm, also known as the Munkres algorithm. The Hungarian algorithm is an efficient method for solving the assignment problem, which is a special case of the minimum weight matching problem.

# Steps:
1. Compute the Manhattan distance matrix between all points in set A and set B.
2. Use the Hungarian algorithm to find the minimum weight matching between the points.
3. Extract the indices of the matched pairs from the minimum weight matching.
4. Return the matched indices.

# Implementation:

```python
import numpy as np
from scipy.optimize import linear_sum_assignment

def compute_manhattan_distance(points1, points2):
    """
    Compute the Manhattan distance matrix between points1 and points2.
    """
    distance_matrix = np.zeros((len(points1), len(points2)))
    for i, p1 in enumerate(points1):
        for j, p2 in enumerate(points2):
            distance_matrix[i, j] = np.sum(np.abs(p1 - p2))
    return distance_matrix

def map_points(points1, points2):
    """
    Map points from set A to set B such that the total Manhattan distance is minimized.
    """
    distance_matrix = compute_manhattan_distance(points1, points2)
    row_ind, col_ind = linear_sum_assignment(distance_matrix)
    return col_ind

# Example usage
points1 = np.array([(1, 2), (2, 3), (3, 1)])
points2 = np.array([(1.8, 2.6), (1.9, 3.4), (3.4, 0.4)])

matched_indices = map_points(points1, points2)
print(matched_indices)  # Output: [2, 0, 1]
```

# Complexity Analysis:
The time complexity of the Hungarian algorithm is O(n^3), where n is the number of points in set A (or set B). Since the given problem involves a small number of data points in 3-dimensional space, the brute force approach using the Hungarian algorithm should be efficient enough.