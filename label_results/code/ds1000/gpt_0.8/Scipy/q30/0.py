One way to make a sparse scipy matrix symmetric is to iterate over the non-zero elements of the matrix and set the corresponding element in the transposed position. 

Here's one possible solution using the `lil_matrix` format:

```python
import numpy as np
from scipy.sparse import lil_matrix

def make_symmetric(matrix):
    num_rows, num_cols = matrix.shape
    for i in range(num_rows):
        for j in matrix.rows[i]:
            if j != i:
                matrix[j, i] = matrix[i, j]
    return matrix

# Example usage
M = lil_matrix((10, 10))
# Populate M with some non-zero values

M = make_symmetric(M)
```

This solution iterates over the rows of the matrix and for each non-zero element, it checks if the corresponding element in the transposed position exists. If it doesn't, it sets it to the same value.

Note that this solution assumes that the matrix is already in the `lil_matrix` format. If you have a different sparse matrix format, you can convert it to `lil_matrix` using the `toarray()` or `tolil()` methods before using the `make_symmetric()` function.