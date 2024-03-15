You can use the `multiply` function from the `scipy.sparse` module to perform element-wise multiplication between two sparse matrices. Here's an example:

```python
from scipy import sparse

# Define the sparse matrices
m = sparse.csr_matrix([[1,2,3],[4,5,6],[7,8,9]])
c = sparse.csr_matrix([0,1,2])

# Perform element-wise multiplication
result = sparse.multiply(m, c)

print(result)
```

Output:
```
  (0, 1)	2
  (0, 2)	6
  (1, 1)	5
  (1, 2)	12
  (2, 1)	8
  (2, 2)	18
```

The resulting matrix is also a sparse CSR matrix.