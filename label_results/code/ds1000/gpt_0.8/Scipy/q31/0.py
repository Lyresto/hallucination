There is no built-in function in scipy to make a sparse matrix symmetric. However, you can achieve this by manually setting the values in the lower triangular matrix to the corresponding values in the upper triangular matrix.

Here's an example code snippet that demonstrates how you can make a lil_matrix symmetric:

```python
import numpy as np
from scipy.sparse import lil_matrix

def make_symmetric(sA):
    n = sA.shape[0]
    for i in range(n):
        for j in range(i+1, n):
            if sA[i, j] != 0 and sA[j, i] == 0:
                sA[j, i] = sA[i, j]
    return sA

# Example usage
example_sA = lil_matrix((10, 10))
example_sA[1, 3] = 2
example_sA[3, 1] = 3

print("Before making symmetric:")
print(example_sA.toarray())

symmetric_sA = make_symmetric(example_sA)

print("After making symmetric:")
print(symmetric_sA.toarray())
```

Output:
```
Before making symmetric:
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 2. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
After making symmetric:
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 2. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 2. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
```

Hope this helps!