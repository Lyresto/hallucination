One possible solution is to use the Hungarian algorithm, also known as the Munkres algorithm, which is an efficient algorithm for solving the assignment problem. The assignment problem is a special case of the transportation problem, where the goal is to minimize the cost of assigning "supplies" to "demands" in a balanced way.

In this case, we can formulate the problem as follows:
- Create a distance matrix where each element represents the Manhattan distance between a point in set A and a point in set B.
- Apply the Hungarian algorithm to find the optimal assignment of points between the two sets, minimizing the total distance.

Here's the code to implement this solution:

```
import numpy as np
from scipy.optimize import linear_sum_assignment

points1 = np.array([(x, y) for x in np.linspace(-1,1,7) for y in np.linspace(-1,1,7)])
N = points1.shape[0]
points2 = 2*np.random.rand(N,2)-1

# Calculate the distance matrix
distance_matrix = np.abs(points1[:, np.newaxis, :] - points2).sum(axis=2)

# Apply the Hungarian algorithm to find the optimal assignment
row_ind, col_ind = linear_sum_assignment(distance_matrix)

# Get the assignment of points in set B to corresponding points in set A
result = col_ind

print(result)
```

The `linear_sum_assignment` function from the `scipy.optimize` module implements the Hungarian algorithm and returns the optimal assignment. In this case, the `result` variable will contain the indices of the points in set B that correspond to each point in set A.