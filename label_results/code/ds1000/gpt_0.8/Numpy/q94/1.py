One way to extract the array into patches of size 2 by 2 without repeating elements is by using the `as_strided` function from the `numpy.lib.stride_tricks` module. Here's how you can do it:

```python
import numpy as np
from numpy.lib.stride_tricks import as_strided

a = np.array([[1,5,9,13],
              [2,6,10,14],
              [3,7,11,15],
              [4,8,12,16]])

patch_size = (2, 2)
patch_stride = a.itemsize * np.array(a.shape)

result = as_strided(a, shape=(a.shape[0] - patch_size[0] + 1, a.shape[1] - patch_size[1] + 1, *patch_size), strides=(patch_stride[0], patch_stride[1], *patch_stride))
```

The `patch_size` variable represents the desired size of each patch, in this case (2, 2). The `patch_stride` variable calculates the strides for each dimension based on the item size of the array.

The `as_strided` function then creates a new view of the array `a` with the desired shape and strides. The shape is determined by subtracting the patch size from the original array shape and adding 1, while the strides are calculated using the patch stride.

The resulting `result` variable will be a 3-dimensional array with the extracted patches.