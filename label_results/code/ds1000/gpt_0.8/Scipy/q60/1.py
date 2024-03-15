You can use the `scipy.interpolate.interp1d` function with the `axis` parameter set to 0 to interpolate over the first axis without using for loops. Here is an example:

```python
import numpy as np
from scipy.interpolate import interp1d

array = np.random.randint(0, 9, size=(10, 10, 10))
x = np.linspace(0, 10, 10)
x_new = np.linspace(0, 10, 100)

f = interp1d(x, array, axis=0)
new_array = f(x_new)
```

In this example, `f` is a callable object that can be used to interpolate the array `array` along the first axis. The resulting `new_array` will have shape `(100, 10, 10)`, representing the interpolated values at the new `x_new` values.