One way to achieve this without using a for loop is to use boolean indexing and the `np.in1d` function.

Here's the solution:

```python
import numpy as np

A = np.array([1,1,2,3,3,3,4,5,6,7,8,8])
B = np.array([1,2,8])

# Use np.in1d to check which values in A are also in B
mask = np.in1d(A, B)

# Use the mask to filter out the values from A
C = A[~mask]

print(C)
```

Output:
```
[3 3 3 4 5 6 7]
```

The `np.in1d` function returns a boolean array indicating which values in `A` are also present in `B`. Then, the `~mask` is used to invert the boolean array, so that `C` contains only the values in `A` that are not in `B`.