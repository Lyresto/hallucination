To perform a weighted two-tailed t-test with unequal sample sizes, you can use the `ttest_ind` function from the `scipy.stats` module. However, since this function requires arrays of equal size, you need to handle the NaN values and resize the arrays accordingly.

Here's a step-by-step solution to calculate the p-value:

```python
import numpy as np
from scipy.stats import ttest_ind

# Generate random data with NaN values
a = np.random.randn(40)
b = 4 * np.random.randn(50)
a[np.random.choice(40, 5)] = np.nan
b[np.random.choice(50, 5)] = np.nan

# Remove NaN values from the data
a = a[~np.isnan(a)]
b = b[~np.isnan(b)]

# Calculate the p-value using the weighted t-test
t_stat, p_value = ttest_ind(a, b, equal_var=False)

p_value
```

The `np.isnan` function is used to create a boolean mask for removing NaN values from the arrays. The `~` operator is used to negate the mask, selecting the non-NaN values. Finally, the `ttest_ind` function is called with the `equal_var` parameter set to `False` to perform a weighted t-test.

Note that the `ttest_ind` function assumes that the samples are independent and come from populations with possibly different means and variances. If your data violates these assumptions, you may need to consider alternative statistical tests.