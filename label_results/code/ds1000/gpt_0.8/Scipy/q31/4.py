One simple and efficient way to make a sparse scipy matrix symmetric is to iterate over the non-zero elements of the matrix and set the corresponding element in the transposed position.

Here's an example implementation:

```python
import numpy as np
from scipy.sparse import lil_matrix

def make_symmetric(sA):
    sA = sA.tolil()  # Convert to lil_matrix if necessary
    for i in range(sA.shape[0]):
        for j in range(i+1, sA.shape[1]):
            if sA[i, j] != 0 and sA[j, i] == 0:
                sA[j, i] = sA[i, j]
    return sA

# Example usage
example_sA = lil_matrix((10, 10))
example_sA[1, 2] = 1
example_sA[3, 4] = 2

symmetric_sA = make_symmetric(example_sA)
print(symmetric_sA.toarray())
```

This will output the following symmetric matrix:

```
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 2. 0. 0. 0. 0. 0.]
 [0. 0. 0. 2. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
```

Note that this implementation only checks if the transposed element is zero before setting it. If you need to handle cases where both elements are non-zero differently, you can modify the inner `if` statement accordingly.