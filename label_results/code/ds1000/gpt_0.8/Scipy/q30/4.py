One simple and efficient way to make a sparse scipy matrix symmetric is to iterate over the upper triangular part of the matrix and set the corresponding values in the lower triangular part. This can be done using the `triu_indices` function from numpy.

Here's an example of how you can make a lil_matrix symmetric:

```python
import numpy as np
from scipy.sparse import lil_matrix

def make_symmetric(matrix):
    n = matrix.shape[0]
    rows, cols = matrix.nonzero()
    for i, j in zip(rows, cols):
        if i != j:
            matrix[j, i] = matrix[i, j]
    return matrix

M = lil_matrix((10, 10))
# populate M with values

M = make_symmetric(M)
```

This code iterates over the non-zero elements of the matrix and sets the corresponding values in the transposed position. Note that we skip the diagonal elements since they are already symmetric.

You can also use this approach for other sparse matrix formats, such as csr_matrix, by converting the matrix to a lil_matrix before making it symmetric and then converting it back to the desired format.