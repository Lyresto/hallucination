To generate a log uniform distribution in Python, you can use the `numpy` library along with the `numpy.random.uniform` function. Here's how you can do it:

```python
import numpy as np

min_val = np.exp(0)  # min value (e.g., exp(min))
max_val = np.exp(1)  # max value (e.g., exp(max))
n = 10000  # number of samples

log_uniform_samples = np.random.uniform(low=min_val, high=max_val, size=n)
```

In the above code, `np.exp(0)` and `np.exp(1)` are used to convert the min and max values to their exponential equivalents. The `np.random.uniform` function then generates `n` samples from a uniform distribution between `min_val` and `max_val`, which effectively gives you a log uniform distribution.

The resulting `log_uniform_samples` variable will contain `n` log uniformly distributed values within the specified range.

Note: Make sure to avoid using variable names like `min` and `max` as they are built-in function names in Python.