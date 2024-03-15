To perform a weighted two-tailed t-test with different sample sizes, you can use the `ttest_ind` function from the `scipy.stats` module. However, since the samples have different sizes and may contain NaN values, you need to preprocess the data before performing the t-test.

Here is a step-by-step approach to calculate the p-value for a weighted two-tailed t-test:

1. Remove NaN values from both samples:
```python
a = a[~np.isnan(a)]
b = b[~np.isnan(b)]
```

2. Calculate the weights for each sample based on their sizes:
```python
weight_a = len(a)
weight_b = len(b)
```

3. Calculate the mean and standard deviation for each sample:
```python
mean_a = np.mean(a)
std_a = np.std(a, ddof=1)
mean_b = np.mean(b)
std_b = np.std(b, ddof=1)
```

4. Calculate the pooled standard deviation using the weights:
```python
pooled_std = np.sqrt(((weight_a-1)*std_a**2 + (weight_b-1)*std_b**2) / (weight_a + weight_b - 2))
```

5. Calculate the t-value using the weighted means, pooled standard deviation, and sample sizes:
```python
t_value = (mean_a - mean_b) / (pooled_std * np.sqrt((1/weight_a) + (1/weight_b)))
```

6. Calculate the degrees of freedom using the sample sizes:
```python
df = weight_a + weight_b - 2
```

7. Calculate the p-value using the t-value and degrees of freedom:
```python
p_value = 2 * (1 - scipy.stats.t.cdf(np.abs(t_value), df))
```

Putting it all together, the code will look like this:

```python
import numpy as np
import scipy.stats

a = np.random.randn(40)
b = 4 * np.random.randn(50)

a = a[~np.isnan(a)]
b = b[~np.isnan(b)]

weight_a = len(a)
weight_b = len(b)

mean_a = np.mean(a)
std_a = np.std(a, ddof=1)
mean_b = np.mean(b)
std_b = np.std(b, ddof=1)

pooled_std = np.sqrt(((weight_a-1)*std_a**2 + (weight_b-1)*std_b**2) / (weight_a + weight_b - 2))

t_value = (mean_a - mean_b) / (pooled_std * np.sqrt((1/weight_a) + (1/weight_b)))

df = weight_a + weight_b - 2

p_value = 2 * (1 - scipy.stats.t.cdf(np.abs(t_value), df))

print("P-value:", p_value)
```

This will calculate and print the p-value for the weighted two-tailed t-test.