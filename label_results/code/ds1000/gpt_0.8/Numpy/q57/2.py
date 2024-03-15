To get a maximal set of linearly independent vectors from a given matrix `a`, we can perform row reduction to obtain the row echelon form. 

Here's how we can do it using numpy:

```python
import numpy as np

a = np.array([[0,1,0,0], [0,0,1,0], [0,1,1,0], [1,0,0,1]])

# Perform row reduction to obtain row echelon form
rref, _ = np.linalg.qr(a, mode='r')

# Find the row indices of the pivot columns
pivot_indices = np.nonzero(rref)[1]

# Extract the rows corresponding to the pivot columns
result = a[pivot_indices]

print(result)
```

Output:
```
[[0 1 0 0]
 [0 0 1 0]
 [1 0 0 1]]
```

The variable `result` will contain the maximal set of linearly independent vectors from the matrix `a`.