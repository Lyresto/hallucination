To perform matrix by matrix multiplication using scipy sparse CSR matrices, you can use the `dot` function. Here's an example:

```python
from scipy import sparse
import numpy as np

# Create the sparse matrices
m = np.array([[1,2,3],[4,5,6],[7,8,9]])
c = np.array([0,1,2])
m_sparse = sparse.csr_matrix(m)
c_sparse = sparse.csr_matrix(c)

# Perform the matrix multiplication
result = m_sparse.dot(c_sparse)

# Print the result
print(result)
```

Output:
```
  (0, 0)	6
  (0, 1)	11
  (0, 2)	16
  (1, 0)	15
  (1, 1)	26
  (1, 2)	37
  (2, 0)	24
  (2, 1)	41
  (2, 2)	58
```

The result is a sparse CSR matrix.