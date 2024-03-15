One way to extract the patches is to use the `as_strided` function from the `numpy.lib.stride_tricks` module. Here's the code to achieve that:

```python
import numpy as np
from numpy.lib.stride_tricks import as_strided

a = np.array([[1,5,9,13],
              [2,6,10,14],
              [3,7,11,15],
              [4,8,12,16]])

patch_size = (2, 2)
stride = a.itemsize * np.array(a.shape)

patches = as_strided(a, shape=(a.shape[0] - patch_size[0] + 1, a.shape[1] - patch_size[1] + 1) + patch_size, strides=stride)

result = patches.reshape((-1,) + patch_size)
```

The `patch_size` variable represents the size of each patch, and `stride` calculates the appropriate strides for the patches.

The `as_strided` function returns a view of the original array with the desired patches. Reshaping the result to `-1` ensures that the patches are flattened into a 3D array.

The resulting `result` variable will contain the desired patches.