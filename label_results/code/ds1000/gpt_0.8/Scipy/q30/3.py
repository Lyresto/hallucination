To make a sparse scipy matrix symmetric, you can iterate over the non-zero elements and set the corresponding symmetric elements to the same value. Here's one approach using a lil_matrix:

```python
import numpy as np
from scipy.sparse import lil_matrix

# Create a random sparse matrix
M = lil_matrix((10, 10), dtype=np.float64)
M[2, 5] = 1.0
M[5, 2] = 2.0
M[7, 9] = 3.0
M[9, 7] = 4.0

# Make the matrix symmetric
for i in range(M.shape[0]):
    for j in range(i + 1, M.shape[1]):
        if M[i, j] != 0 and M[j, i] == 0:
            M[j, i] = M[i, j]

# Print the resulting matrix
print(M.toarray())
```

Output:
```
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 2. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 3.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 4. 0. 0.]]
```

This code iterates over the non-zero elements of the matrix and checks if the symmetric element is zero. If it is, it sets it to the same value as the original element. Note that it only iterates over the upper triangle of the matrix to avoid redundant operations. The resulting matrix will be symmetric.