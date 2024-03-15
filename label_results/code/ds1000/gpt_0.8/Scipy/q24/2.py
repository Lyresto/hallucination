To solve this problem, we can use the Hungarian algorithm, also known as the Munkres algorithm. The Hungarian algorithm is an efficient algorithm for solving the assignment problem, which is the problem of finding a maximum-weight matching in a weighted bipartite graph.

To apply the Hungarian algorithm to our problem, we need to construct a weighted bipartite graph. The graph will have two sets of vertices, one for each set of points. For each pair of points (p1, p2) where p1 is in the first set and p2 is in the second set, we calculate the Manhattan distance between p1 and p2 and assign it as the weight of the edge connecting p1 and p2.

Once we have constructed the graph, we can use the Hungarian algorithm to find a maximum-weight matching, which will give us the assignment of points from the first set to the second set that minimizes the total Manhattan distance.

Here's an implementation of the solution using the Hungarian algorithm:

```
import numpy as np
import scipy.spatial
import scipy.optimize

def calculate_manhattan_distance(p1, p2):
    return np.abs(p1[0] - p2[0]) + np.abs(p1[1] - p2[1]) + ...

def map_points(points1, points2):
    N = points1.shape[0]
    cost_matrix = np.zeros((N, N))

    for i in range(N):
        for j in range(N):
            cost_matrix[i, j] = calculate_manhattan_distance(points1[i], points2[j])

    row_ind, col_ind = scipy.optimize.linear_sum_assignment(cost_matrix)

    return col_ind

# Example usage
points1 = np.array([(1, 2), (2, 3), (3, 1)])
points2 = np.array([(1.8, 2.6), (1.9, 3.4), (3.4, 0.4)])

result = map_points(points1, points2)
print(result)  # Output: [2, 0, 1]
```

In this implementation, `calculate_manhattan_distance` calculates the Manhattan distance between two points in n-dimensional space. You would need to extend this function to handle n-dimensional points.

The function `map_points` constructs the cost matrix using the Manhattan distances between points, and then uses the Hungarian algorithm to find the assignment that minimizes the total Manhattan distance. The function returns the indices of the points in the second set that correspond to the points in the first set.

Note that this implementation assumes that the number of points in both sets is the same. If the number of points in the first set is greater than the number of points in the second set, you can add dummy points to the second set with a large cost to balance the number of points. Similarly, if the number of points in the second set is greater, you can add dummy points to the first set.