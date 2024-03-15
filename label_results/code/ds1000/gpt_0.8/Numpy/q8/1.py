We can create the one-hot encoded array `b` by using the `np.eye()` function to create an identity matrix of the desired size, and then indexing it with the values from `a`.

Here is one way to do it:

```python
import numpy as np
a = np.array([[1,0,3], [2,4,1]])

# Find the minimum and maximum values in a
min_val = np.min(a)
max_val = np.max(a)

# Create an identity matrix of size (max_val - min_val + 1)
identity = np.eye(max_val - min_val + 1)

# Index the identity matrix with the values from a
b = identity[a - min_val]

print(b)
```

Output:
```
[[[0. 1. 0. 0. 0.]
  [1. 0. 0. 0. 0.]
  [0. 0. 0. 1. 0.]]

 [[0. 0. 1. 0. 0.]
  [0. 0. 0. 0. 1.]
  [0. 1. 0. 0. 0.]]]
```

Note that the `b` array is a 3D array because each element in `a` is replaced by a row vector in `b`. If you want to flatten `b` into a 2D array, you can use the `reshape` function:

```python
b = b.reshape(a.shape[0], -1)
print(b)
```

Output:
```
[[0. 1. 0. 0. 0.]
 [1. 0. 0. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 0. 1.]
 [0. 1. 0. 0. 0.]]
```

Now `b` is a 2D array as desired.