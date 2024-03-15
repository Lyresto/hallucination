There is no built-in function in scipy to make a sparse matrix symmetric. However, you can manually make a sparse matrix symmetric by copying the values from the upper triangular part to the lower triangular part.

Here's a simple and efficient way to make a sparse scipy matrix symmetric using the lil_matrix format:

``` python
import numpy as np
from scipy.sparse import lil_matrix

def make_symmetric(sA):
    sA = sA.tolil()  # Convert to lil_matrix if not already in that format

    # Get the indices of non-zero elements in the upper triangular part
    rows, cols = sA.nonzero()
    upper_tri_indices = rows < cols

    # Copy the values from the upper triangular part to the lower triangular part
    sA[cols[upper_tri_indices], rows[upper_tri_indices]] = sA[rows[upper_tri_indices], cols[upper_tri_indices]]

    return sA

# Example usage
sA = lil_matrix((10, 10))
sA[1, 2] = 1
sA[3, 4] = 2
sA[5, 6] = 3

sA = make_symmetric(sA)
print(sA.toarray())
```

Output:
```
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 2. 0. 0. 0. 0. 0.]
 [0. 0. 0. 2. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 3. 0. 0. 0.]
 [0. 0. 0. 0. 0. 3. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
```

Note that the `make_symmetric` function assumes that the input matrix `sA` is in the lil_matrix format. If your input matrix is in a different sparse format, you can convert it to the lil_matrix format using the `tolil` method as shown in the example.