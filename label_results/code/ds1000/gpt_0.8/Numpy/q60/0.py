One way to solve this problem is by using the `ttest_ind` function from the `scipy.stats` module. However, since the sizes of the samples are different, we need to account for the difference in sample sizes by using the `equal_var=False` argument in the `ttest_ind` function.

Additionally, we need to remove any NaN values from the original data arrays before performing the t-test.

Here's how you can calculate the p-value for the weighted two-tailed t-test:

```python
import numpy as np
import scipy.stats

a = np.random.randn(40)
b = 4*np.random.randn(50)

# Remove NaN values from the original data arrays
a = a[~np.isnan(a)]
b = b[~np.isnan(b)]

# Perform the two-tailed t-test
t_stat, p_value = scipy.stats.ttest_ind(a, b, equal_var=False)

print("p-value:", p_value)
```

This will give you the p-value for the weighted two-tailed t-test.