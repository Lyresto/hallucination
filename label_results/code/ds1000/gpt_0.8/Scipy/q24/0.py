One possible solution to this problem is to use the Hungarian algorithm, also known as the Munkres algorithm. This algorithm is used to solve the assignment problem, which is a special case of the transportation problem.

To apply the Hungarian algorithm to our problem, we need to define a cost matrix where each element represents the distance between two points. In this case, we can use the Manhattan distance as the cost metric. Once we have the cost matrix, we can use the Hungarian algorithm to find the optimal assignment that minimizes the total cost.

Here's how you can implement this solution in Python:

```python
import numpy as np
import scipy.spatial
import scipy.optimize

# Define the cost matrix
cost_matrix = scipy.spatial.distance.cdist(points1, points2, metric='cityblock')

# Use the Hungarian algorithm to find the optimal assignment
row_ind, col_ind = scipy.optimize.linear_sum_assignment(cost_matrix)

# Get the assignment as a list
assignment = col_ind.tolist()

# Print the assignment
print(assignment)
```

This will give you the optimal assignment of points from set "A" to set "B" that minimizes the total Manhattan distance.

Note that the Hungarian algorithm has a time complexity of O(n^3), where n is the number of points. In your case, where you mentioned that you have a small number of data points, this should be efficient enough. However, if you have a large number of points, you might need to consider other algorithms with better time complexity.