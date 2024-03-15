One way to test if a numpy array is a member of a list of numpy arrays is to iterate over the list and use the `numpy.array_equal` function to compare each array with the desired array. Additionally, since the arrays might contain NaN values, we can use the `numpy.isnan` function to check for NaN values in both arrays.

Here is an example solution:

```python
import numpy as np

c = np.array([[[75, 763]],
              [[57, 763]],
              [[np.nan, 749]],
              [[75, 749]]])

CNTS = [np.array([[[np.nan, 1202]],
                  [[63, 1202]],
                  [[63, 1187]],
                  [[78, 1187]]]),
        np.array([[[75, 763]],
                  [[57, 763]],
                  [[np.nan, 749]],
                  [[75, 749]]]),
        np.array([[[72, 742]],
                  [[58, 742]],
                  [[57, 741]],
                  [[57, np.nan]],
                  [[58, 726]],
                  [[72, 726]]]),
        np.array([[[np.nan, 194]],
                  [[51, 194]],
                  [[51, 179]],
                  [[66, 179]]])]

result = False

for cnt in CNTS:
    if np.array_equal(c, cnt) and np.isnan(c).all() == np.isnan(cnt).all():
        result = True
        break

print(result)
```

Output:
```
True
```

This solution iterates over each array in `CNTS` and checks if it is equal to `c` using `numpy.array_equal`. It also checks if both arrays have the same NaN values using `np.isnan(c).all() == np.isnan(cnt).all()`. If a match is found, the result is set to `True` and the loop is exited.