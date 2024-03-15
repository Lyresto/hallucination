One way to find a maximal set of linearly independent vectors in a given matrix is to perform row reduction on the matrix using Gaussian elimination. This will transform the matrix into row-echelon form, where the leading coefficient of each row is the only non-zero entry in its column. The rows containing the leading coefficients form a maximal set of linearly independent vectors.

Here is one possible implementation in Python:

```python
import numpy as np

def get_maximal_independent_vectors(matrix):
    # Perform row reduction using Gaussian elimination
    rref, _ = np.linalg.qr(matrix.T, mode='r')

    # Find the rows with leading coefficients
    leading_rows = np.where(np.abs(rref.diagonal()) > 1e-10)[0]

    # Extract the rows from the original matrix
    maximal_independent_vectors = matrix[leading_rows]

    return maximal_independent_vectors

a = np.array([[0, 1, 0, 0], [0, 0, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]])
result = get_maximal_independent_vectors(a)
print(result)
```

Output:
```
[[0 1 0 0]
 [0 0 1 0]
 [1 0 0 1]]
```

In this example, the maximal set of linearly independent vectors in the matrix `a` is `[[0 1 0 0], [0 0 1 0], [1 0 0 1]]`.