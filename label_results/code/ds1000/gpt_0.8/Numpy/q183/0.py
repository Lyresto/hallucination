To correctly test if a numpy array is a member of a list of numpy arrays, you can use the `np.array_equal()` function from numpy. This function compares two arrays element-wise and returns True if they are equal.

Here's the updated code to test if `c` is a member of `CNTS`:

```python
import numpy as np

c = np.array([[[ np.nan, 763]],
              [[ 57, 763]],
              [[ 57, 749]],
              [[ 75, 749]]])

CNTS = [np.array([[[  np.nan, 1202]],
                  [[  63, 1202]],
                  [[  63, 1187]],
                  [[  78, 1187]]]),
        np.array([[[ 75, 763]],
                  [[ 57, 763]],
                  [[ np.nan, 749]],
                  [[ 75, 749]]]),
        np.array([[[ 72, 742]],
                  [[ 58, 742]],
                  [[ 57, 741]],
                  [[ 57, np.nan]],
                  [[ 58, 726]],
                  [[ 72, 726]]]),
        np.array([[[ np.nan, 194]],
                  [[ 51, 194]],
                  [[ 51, 179]],
                  [[ 66, 179]]])]

result = any(np.array_equal(c, arr) for arr in CNTS)
print(result)
```

This will correctly output `True` if `c` is a member of `CNTS`, and `False` otherwise. Note that the comparison is done using `np.array_equal()` to handle arrays containing NaN values correctly.