Here's one way to perform matrix by matrix multiplication using a sparse CSR matrix in scipy:

```python
from scipy import sparse

m = sparse.csr_matrix([[1,2,3],[4,5,6],[7,8,9]])
c = sparse.csr_matrix([[0,1,2]])

result = m.multiply(c)
```

The `multiply()` method is used to perform element-wise multiplication between the two matrices. The result will also be a sparse CSR matrix.

Note that in this example, `c` is a 2D matrix with shape (1,3) instead of a 1D array. This is because sparse matrix operations in scipy typically expect 2D matrices.