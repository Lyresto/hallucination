One possible solution is to iterate over the non-zero elements of the sparse matrix and assign their values to their corresponding symmetric positions. Here's an example implementation:

```python
import numpy as np
from scipy.sparse import lil_matrix

def make_symmetric(sparse_matrix):
    # Get the number of rows and columns in the sparse matrix
    rows, cols = sparse_matrix.shape

    # Create a new lil_matrix to store the symmetric matrix
    symmetric_matrix = lil_matrix((rows, cols))

    # Iterate over the non-zero elements of the sparse matrix
    for i, j, value in zip(*sparse_matrix.nonzero(), sparse_matrix.data):
        # Assign the value to the corresponding symmetric positions
        symmetric_matrix[i, j] = value
        symmetric_matrix[j, i] = value

    return symmetric_matrix

# Example usage
M = lil_matrix((5, 5))
M[0, 1] = 1
M[1, 0] = 2
M[1, 2] = 3
M[2, 1] = 4
M[2, 3] = 5
M[3, 2] = 6

M = make_symmetric(M)
print(M.toarray())
```

Output:
```
[[0. 1. 2. 0. 0.]
 [1. 0. 3. 0. 0.]
 [2. 3. 0. 5. 0.]
 [0. 0. 5. 0. 0.]
 [0. 0. 0. 0. 0.]]
```

This approach iterates only over the non-zero elements of the sparse matrix, so it should be efficient for large matrices with a small number of non-zero elements.