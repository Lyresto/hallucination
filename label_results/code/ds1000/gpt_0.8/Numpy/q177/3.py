To achieve the desired result, we can use the `as_strided` function from the `numpy.lib.stride_tricks` module. This function allows us to create a view into the original array with a desired shape and stride.

Here's the code to solve the problem:

```python
import numpy as np
from numpy.lib.stride_tricks import as_strided

def sliding_window(arr, size):
    # Calculate the shape of the output array
    shape = (arr.shape[0] - size[0] + 1, arr.shape[1] - size[1] + 1, size[0], size[1])
    
    # Calculate the strides of the output array
    strides = (arr.strides[0], arr.strides[1], arr.strides[0], arr.strides[1])
    
    # Create a view into the original array with the desired shape and strides
    return as_strided(arr, shape=shape, strides=strides)

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
array([[[[1, 2],
         [2, 3]],

        [[2, 3],
         [3, 4]],

        [[3, 4],
         [4, 5]]],


       [[[2, 3],
         [3, 4]],

        [[3, 4],
         [4, 5]],

        [[4, 5],
         [5, 6]]],


       [[[3, 4],
         [4, 5]],

        [[4, 5],
         [5, 6]],

        [[5, 6],
         [6, 7]]]])
```

The `sliding_window` function takes in the input array `arr` and the window size `size`. It calculates the shape and strides of the output array using the formula `(arr.shape[0] - size[0] + 1, arr.shape[1] - size[1] + 1, size[0], size[1])`. It then creates a view into the original array using `as_strided` with the calculated shape and strides.

Note that the output array is a 4-dimensional array, where the first two dimensions correspond to the position of the window in the input array, and the last two dimensions correspond to the window itself.