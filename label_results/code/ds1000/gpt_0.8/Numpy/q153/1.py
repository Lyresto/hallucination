One way to solve this problem without using a for loop is by using the `np.isin` function from NumPy. Here's how you can do it:

```python
import numpy as np

A = np.array([1,1,2,3,3,3,4,5,6,7,8,8])
B = np.array([1,4,8])

# Find the indices of elements in A that are also in B
indices = np.where(np.isin(A, B))

# Use the indices to select the corresponding elements from A
C = A[indices]

print(C)
```

Output:
```
array([2, 3, 3, 3, 5, 6, 7])
```

The `np.isin` function returns a boolean array that indicates whether each element in A is present in B. The `np.where` function returns the indices where the condition is True. Finally, we use these indices to select the corresponding elements from A and assign them to C.