The correct way to test if a numpy array is a member of a list of numpy arrays is to use the np.array_equal() function. Here is the updated code:

```python
import numpy as np

c = np.array([[[ 75, 763]],
              [[ 57, 763]],
              [[ 57, 749]],
              [[ 75, 749]]])

CNTS = [np.array([[[  78, 1202]],
                  [[  63, 1202]],
                  [[  63, 1187]],
                  [[  78, 1187]]]),
        np.array([[[ 75, 763]],
                  [[ 57, 763]],
                  [[ 57, 749]],
                  [[ 75, 749]]]),
        np.array([[[ 72, 742]],
                  [[ 58, 742]],
                  [[ 57, 741]],
                  [[ 57, 727]],
                  [[ 58, 726]],
                  [[ 72, 726]]]),
        np.array([[[ 66, 194]],
                  [[ 51, 194]],
                  [[ 51, 179]],
                  [[ 66, 179]]])]

result = np.any([np.array_equal(c, cnt) for cnt in CNTS])
print(result)
```

Output:
```
True
```

This will correctly test if `c` is a member of `CNTS` and return `True` in this case.