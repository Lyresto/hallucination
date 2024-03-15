To test if a numpy array is a member of a list of numpy arrays, you can use the `np.array_equal()` function to compare each array in the list with the given array. Additionally, you can use the `np.isnan()` function to handle arrays that contain NaN values.

Here is the modified code:

```python
import numpy as np

c = np.array([[[ 75, 763]],
              [[ 57, 763]],
              [[ np.nan, 749]],
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

result = False
for cnt in CNTS:
    if np.array_equal(c, cnt) and np.isnan(c).all() == np.isnan(cnt).all():
        result = True
        break

print(result)
```

The output of the code above will be `True` if the array `c` is present in the list `CNTS`, and `False` otherwise. The `np.isnan()` function is used to compare the NaN values in the arrays.