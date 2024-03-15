To find the relative extrema of a given array, we can use the `scipy.signal.argrelmin` and `scipy.signal.argrelmax` functions. These functions return the indices of the relative minimum and maximum points in the array respectively.

Here is the updated code:

```python
import numpy as np
from scipy import signal

arr = np.array([-624.59309896, -624.59309896, -624.59309896, -625., -625., -625.,])
n = 2

local_minima = signal.argrelmin(arr, order=n)[0]
local_maxima = signal.argrelmax(arr, order=n)[0]

result = np.concatenate((local_minima, local_maxima))
```

The `signal.argrelmin` function returns the indices of the relative minima in the array, and the `signal.argrelmax` function returns the indices of the relative maxima in the array. We then concatenate the indices of both minima and maxima to get the final result.

Note: In the given example, all the elements in the array are the same, so there are no relative extrema. Therefore, the result will be an empty array.

```python
result = []
```

If you run the code with a different array that has relative extrema, the result will contain the indices of those extrema.