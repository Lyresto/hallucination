To make a sparse scipy matrix symmetric, you can use the following steps:

1. Convert the matrix to a coo_matrix format using the `tocoo()` method.
2. Create a new coo_matrix by concatenating the existing matrix with its transpose using the `hstack()` and `vstack()` methods.
3. Convert the new coo_matrix back to the original format using the `tolil()` or `tocsr()` method.

Here is the code to accomplish this:

```python
import numpy as np
from scipy.sparse import lil_matrix, coo_matrix

# Create a lil_matrix as an example
M = lil_matrix((10, 10))
M[0, 1] = 1
M[2, 3] = 2

# Convert M to coo_matrix format
M_coo = M.tocoo()

# Create a new coo_matrix by concatenating M with its transpose
M_symmetric_coo = coo_matrix((np.concatenate((M_coo.data, M_coo.data)),
                              (np.concatenate((M_coo.row, M_coo.col)),
                               np.concatenate((M_coo.col, M_coo.row)))),
                             shape=M_coo.shape)

# Convert the new coo_matrix back to lil_matrix format
M_symmetric = M_symmetric_coo.tolil()
```

Now, `M_symmetric` is a lil_matrix that is symmetric, where `M_symmetric[i, j]` is equal to `M_symmetric[j, i]` for any `i` and `j`.