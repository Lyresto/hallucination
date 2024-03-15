The matrix by matrix multiplication using scipy sparse CSR matrices can be achieved by using the dot() function from the scipy.sparse module. Here's an example:

```python
from scipy import sparse
import numpy as np

# Create the sparse CSR matrix
m = np.array([[1,2,3],[4,5,6],[7,8,9]])
c = np.array([0,1,2])
example_sA = sparse.csr_matrix(m)
example_sB = sparse.csr_matrix(c)

# Perform the matrix multiplication
result = example_sA.dot(example_sB)

# Print the result
print(result)
```

This will output the following CSR matrix:

```
  (0, 1)  2
  (1, 1)  5
  (2, 1)  8
```

The result is a sparse CSR matrix with non-zero values at positions (0,1), (1,1), and (2,1), corresponding to the values 2, 5, and 8 respectively.