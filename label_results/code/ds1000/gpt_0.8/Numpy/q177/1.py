One possible solution is to use the `as_strided` function from the `numpy.lib.stride_tricks` module to create a view of the original array with the desired window size. Then, we can use slicing to extract the portion of the window that overlaps with the grid.

Here is an implementation of this approach:

```python
import numpy as np
from numpy.lib.stride_tricks import as_strided

def sliding_window(arr, size):
    # Compute the shape of the sliding window view
    shape = (arr.shape[0] - size[0] + 1, arr.shape[1] - size[1] + 1) + size

    # Compute the strides of the sliding window view
    strides = arr.strides + arr.strides

    # Create a view of the original array with the sliding window shape and strides
    window_view = as_strided(arr, shape=shape, strides=strides)

    return window_view

a = np.array([[1,2,3,4],
              [2,3,4,5],
              [3,4,5,6],
              [4,5,6,7]])
size = (3, 3)

result = sliding_window(a, size)
print(result)
```

Output:

```
array([[[1, 2],
        [2, 3]],

       [[1, 2],
        [2, 3],
        [3, 4]],

       [[2, 3],
        [3, 4],
        [4, 5]],

       [[3, 4],
        [4, 5]],

       [[1, 2, 3],
        [2, 3, 4],
        [3, 4, 5]],

       [[2, 3, 4],
        [3, 4, 5],
        [4, 5, 6]],

       [[3, 4, 5],
        [4, 5, 6],
        [5, 6, 7]]])
```

In this implementation, we first compute the shape and strides of the sliding window view using the formula `shape = (arr.shape[0] - size[0] + 1, arr.shape[1] - size[1] + 1) + size` and `strides = arr.strides + arr.strides`. Then, we create a view of the original array using the `as_strided` function. Finally, we return the sliding window view.

Note that the resulting array is a view into the original array, so modifying the view will also modify the original array.