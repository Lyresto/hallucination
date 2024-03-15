One possible solution to this problem is to use the Hungarian algorithm, also known as the Munkres algorithm. The Hungarian algorithm is an efficient algorithm for solving the assignment problem, which is a special case of the bipartite matching problem.

The assignment problem can be formulated as follows:
- Let A be the first set of points and B be the second set of points.
- Let D be an n x n matrix, where D[i][j] represents the Manhattan distance between point A[i] and point B[j].
- The goal is to find a matching between points in A and points in B such that each point is only used once and the total distance is minimized.

The Hungarian algorithm works by finding an optimal assignment that minimizes the total cost. It does this by iteratively updating a matrix of costs and potentials, and finding a sequence of augmenting paths that improves the current assignment. The algorithm terminates when no more augmenting paths can be found.

To use the Hungarian algorithm in Python, you can use the `scipy.optimize.linear_sum_assignment` function, which implements the algorithm. Here's an example of how you can use it to solve the problem:

```python
import numpy as np
from scipy.optimize import linear_sum_assignment

# Define the points in A and B
points1 = np.array([(x, y) for x in np.linspace(-1,1,7) for y in np.linspace(-1,1,7)])
N = points1.shape[0]
points2 = 2*np.random.rand(N,2)-1

# Calculate the distance matrix
dist_matrix = scipy.spatial.distance.cdist(points1, points2, metric='cityblock')

# Solve the assignment problem using the Hungarian algorithm
row_ind, col_ind = linear_sum_assignment(dist_matrix)

# Get the assignment of points in B to corresponding points in A
assignment = col_ind.tolist()
print(assignment)
```

The `linear_sum_assignment` function returns the optimal assignment of points in B to points in A as a tuple of two arrays: `row_ind` and `col_ind`. The `col_ind` array contains the indices of the points in B that are assigned to each point in A. In the example above, `assignment` will contain the assignment of points in B to points in A.

Note that the Hungarian algorithm has a time complexity of O(n^3), where n is the number of points. Therefore, it should be efficient for small numbers of datapoints in 3-dimensional space, as you mentioned in your question.