One possible solution is to use the `np.eye()` function to create a 2D array of one-hot vectors for each element in `a`. Then, we can use `np.concatenate()` to combine these one-hot vectors into a single 2D one-hot array.

Here's the code to achieve this:

```python
import numpy as np

a = np.array([[1,0,3], [2,4,1]])

# Find the range of values in a
min_val = np.min(a)
max_val = np.max(a)

# Create a one-hot array for each element in a
one_hot_arrays = [np.eye(max_val - min_val + 1)[row - min_val] for row in a.flatten()]

# Combine the one-hot arrays into a single 2D one-hot array
b = np.concatenate(one_hot_arrays).reshape(a.shape[0], a.shape[1], -1)

print(b)
```

Output:
```
array([[[0., 1., 0., 0., 0.],
        [1., 0., 0., 0., 0.],
        [0., 0., 0., 1., 0.]],

       [[0., 0., 1., 0., 0.],
        [0., 0., 0., 0., 1.],
        [0., 1., 0., 0., 0.]]])
```

This code first calculates the range of values in `a` (from the minimum value to the maximum value) using `np.min()` and `np.max()`. Then, it creates a one-hot array for each element in `a` using `np.eye()` and `row - min_val` to shift the one-hot encoding. Finally, it concatenates these one-hot arrays using `np.concatenate()` and reshapes the resulting array to match the shape of `a`.