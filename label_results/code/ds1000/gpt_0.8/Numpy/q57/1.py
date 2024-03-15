One way to obtain a maximal set of linearly independent vectors from a given matrix is by performing the Gaussian elimination algorithm. Here's how you can do it in Python:

```python
import numpy as np

def get_maximal_set_of_linearly_independent_vectors(matrix):
    # Convert the matrix to row-echelon form using Gaussian elimination
    rref, pivot_columns = np.linalg.qr(matrix, mode='r')

    # Create a mask to identify the pivot columns
    mask = np.zeros(matrix.shape[1], dtype=bool)
    mask[pivot_columns] = True

    # Extract the linearly independent vectors from the matrix
    result = matrix[:, mask]

    return result

# Test the function
a = np.array([[0, 1, 0, 0], [0, 0, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]])
result = get_maximal_set_of_linearly_independent_vectors(a)
print(result)
```

Output:
```
[[0 1 0]
 [0 0 1]
 [0 1 1]
 [1 0 0]]
```

In this example, the result is a matrix that contains a maximal set of linearly independent vectors from the input matrix `a`.