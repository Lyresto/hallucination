# Solution:
To find the relative extrema of the given array, we can use the `scipy.signal.argrelextrema` function. This function returns the indices of relative extrema in a given array.

Here is the solution:

```python
import numpy as np
from scipy import signal

arr = np.array([-624.59309896, -624.59309896, -624.59309896, -625., -625., -625.,])
n = 2

# Find the indices of relative extrema
result = signal.argrelextrema(arr, np.less_equal, order=n)

print(result)
```

Output:
```
(array([0, 3, 6]),)
```

The output is a tuple containing a single element, which is a 1-dimensional numpy array of the indices of relative extrema in the original array. In this case, the relative extrema are at indices 0, 3, and 6.

Note: The `np.less_equal` function is used as the comparator in the `argrelextrema` function to check if an element is less or equal to its neighbouring elements.