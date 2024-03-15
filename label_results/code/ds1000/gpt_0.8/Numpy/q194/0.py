To multiply the values of matrix A along the third dimension with matrix B, you can use the `np.matmul()` function. Here's how you can do it:

```python
import numpy as np

A = np.random.rand(5, 6, 3)
B = np.random.rand(3, 3)

result = np.matmul(A, B)

print(result.shape)  # shape will be (5, 6, 3)
```

This will give you a matrix of shape (x, y, 3) where the values of the third dimension of A are multiplied by matrix B.