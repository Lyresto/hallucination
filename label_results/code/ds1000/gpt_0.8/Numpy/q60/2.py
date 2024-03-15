# Solution:
To perform a weighted two-tailed t-test, you can use the `ttest_ind` function from the `scipy.stats` module. However, as you mentioned, the two samples need to have equal sizes. To overcome this, you can use the `nanmean` and `nanstd` functions from the `numpy` module to calculate the mean and standard deviation of each sample, while ignoring any `nan` values.

Here's how you can calculate the p-value for a two-tailed t-test:

```python
import numpy as np
from scipy.stats import ttest_ind

# Generate random data for sample 1 and sample 2
a = np.random.randn(40)
b = 4 * np.random.randn(50)

# Calculate the mean and standard deviation for each sample, ignoring nans
mean_a = np.nanmean(a)
std_a = np.nanstd(a)
mean_b = np.nanmean(b)
std_b = np.nanstd(b)

# Calculate the p-value for the two-tailed t-test
t_stat, p_value = ttest_ind(a, b, equal_var=False)

# Print the p-value
print("p-value:", p_value)
```

Note that we set `equal_var=False` in the `ttest_ind` function since the variances of the two samples are not assumed to be equal.

Hope this helps! Let me know if you have any further questions.