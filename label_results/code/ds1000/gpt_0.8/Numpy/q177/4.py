To achieve the desired result, you can use `scipy.ndimage.generic_filter` function from the `scipy` library. This function allows you to apply a custom function to each element in a N-dimensional array while considering the neighborhood around each element.

Here's how you can implement it for your specific problem:

```python
import numpy as np
from scipy.ndimage import generic_filter

a = np.array([[1,2,3,4],
              [2,3,4,5],
              [3,4,5,6],
              [4,5,6,7]])
size = (3, 3)

def moving_window(arr):
    window = arr.reshape(size)
    return window

result = generic_filter(a, moving_window, size=size, mode='constant', cval=0)
```

The `moving_window` function takes a 1D array as input and reshapes it to the desired window size. This function will be applied to each element in the input array `a` using the `generic_filter` function.

The `size` parameter specifies the size of the moving window. The `mode` parameter is set to `'constant'` to handle edge effects by padding the array with zeros. The `cval` parameter specifies the value used for padding.

The resulting `result` array will contain the desired series of arrays/views into the original array, where each element corresponds to the moving window centered at that point.

Note: The `generic_filter` function iterates over each element in the input array, so it may not be the most efficient solution for very large arrays. However, it provides a vectorized approach that handles edge effects and returns the desired result.