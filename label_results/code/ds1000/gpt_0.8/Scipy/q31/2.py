To make a sparse scipy matrix symmetric, you can iterate over the non-zero elements of the matrix and set the corresponding element at [col, row] to be equal to the element at [row, col]. Here's an example implementation for a lil_matrix:

```python
import numpy as np
from scipy.sparse import lil_matrix

def make_symmetric(sA):
    for row in range(sA.shape[0]):
        for col in range(sA.shape[1]):
            if sA[row, col] != 0 and sA[col, row] == 0:
                sA[col, row] = sA[row, col]
    return sA
```

You can use this function to make your lil_matrix symmetric:

```python
sA = lil_matrix((10, 10))
# populate sA
sA = make_symmetric(sA)
```

Note that this implementation assumes that the matrix is square and that the diagonal elements (sA[i, i]) are always present. If your matrix is not square or does not have diagonal elements, you may need to modify the implementation accordingly.