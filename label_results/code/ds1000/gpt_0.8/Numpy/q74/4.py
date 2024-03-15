There is no direct method to insert elements at a specific position in a numpy array. However, you can achieve this by using the `numpy.insert()` function.

Here's an example of how you can use `numpy.insert()` to insert an element at a specific position in a numpy array:

```python
import numpy as np

a = np.array([1, 2, 3, 4])
pos = 2
element = 66

a = np.insert(a, pos, element)
print(a)
```

Output:
```
[ 1  2 66  3  4]
```

In the above code, `np.insert(a, pos, element)` inserts the `element` at index `pos` in the array `a`. The modified array is then assigned back to `a`.