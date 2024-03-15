To perform a weighted two-tailed t-test, you can use the `scipy.stats.ttest_ind` function. However, as you mentioned, the two samples need to be of equal size. In order to handle this discrepancy, you can use the `nanmean` and `nanstd` functions from the `numpy` library to compute the mean and standard deviation while ignoring any NaN values in the data.

Here's an example of how you can calculate the p-value:

```python
import numpy as np
from scipy.stats import ttest_ind

a = np.random.randn(40)
b = 4 * np.random.randn(50)

# Remove NaN values from the data
a = a[~np.isnan(a)]
b = b[~np.isnan(b)]

# Calculate the weighted mean and standard deviation
mean_a = np.nanmean(a)
mean_b = np.nanmean(b)
std_a = np.nanstd(a)
std_b = np.nanstd(b)

# Calculate the sample sizes
n_a = len(a)
n_b = len(b)

# Calculate the degrees of freedom
df = n_a + n_b - 2

# Calculate the standard error
se = np.sqrt(((n_a - 1) * std_a ** 2 + (n_b - 1) * std_b ** 2) / df * (1 / n_a + 1 / n_b))

# Calculate the t-value
t_value = (mean_a - mean_b) / se

# Calculate the p-value
p_value = 2 * (1 - ttest_ind(a, b, equal_var=False)[1])

print(p_value)
```

This code first removes any NaN values from the data using the `~np.isnan()` function. Then, it calculates the weighted means and standard deviations of the two samples using `np.nanmean()` and `np.nanstd()`. The sample sizes are obtained using the `len()` function, and the degrees of freedom are calculated as `n_a + n_b - 2`.

The standard error is computed based on the formula for two independent samples with unequal variances. Finally, the t-value is calculated as the difference in means divided by the standard error. The p-value is then obtained by multiplying the p-value returned by the `ttest_ind` function by 2 to get the two-tailed p-value.

Note that the `equal_var=False` argument is passed to the `ttest_ind` function to indicate that the variances of the two samples are not assumed to be equal.

I hope this helps! Let me know if you have any further questions.