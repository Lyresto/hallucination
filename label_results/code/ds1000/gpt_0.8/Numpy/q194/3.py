To achieve the desired result, you can use the `np.matmul()` function to perform matrix multiplication along the third dimension of matrix A and matrix B. Here's the modified code:

```python
import numpy as np

A = np.random.rand(5, 6, 3)
B = np.random.rand(3, 3)

result = np.matmul(A, B)
```

In this code, `np.matmul(A, B)` multiplies the third dimension of matrix A with matrix B, producing a matrix with the shape (5, 6, 3). This is equivalent to multiplying each "RGB" value in A with matrix B.

Note that the dimensions of matrix B are compatible with the matrix multiplication operation.