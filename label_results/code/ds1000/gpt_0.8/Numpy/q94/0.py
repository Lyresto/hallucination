You can use the `numpy.reshape()` function to achieve this. Here's the code:

```python
import numpy as np

a = np.array([[1,5,9,13],
              [2,6,10,14],
              [3,7,11,15],
              [4,8,12,16]])

result = np.reshape(a, (int(a.shape[0]/2), 2, 2))
```

Explanation:
- The `numpy.reshape()` function reshapes the array `a` into the specified shape.
- We use `int(a.shape[0]/2)` to determine the number of 2x2 patches based on the number of rows in `a`.
- The shape `(int(a.shape[0]/2), 2, 2)` specifies that the resulting array should have `int(a.shape[0]/2)` patches, each of size 2x2.

Note that the resulting array `result` will be a 3-dimensional numpy array.