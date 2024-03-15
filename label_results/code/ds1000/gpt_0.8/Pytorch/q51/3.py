One way to solve this problem is to convert the tensors to numpy arrays and then use numpy functions to count the number of equal elements. Here's one possible solution:

```python
import numpy as np
import torch

def Count(A, B):
    # Convert tensors to numpy arrays
    A_np = A.numpy()
    B_np = B.numpy()
    
    # Count the number of equal elements
    cnt_equal = np.sum(A_np == B_np)
    
    return cnt_equal
```

In this solution, we first convert the tensors `A` and `B` to numpy arrays using the `numpy()` method. Then, we use the `==` operator to compare the elements of the two arrays, which returns a boolean array indicating whether the elements are equal or not. Finally, we use the `sum()` function from numpy to count the number of `True` values in the boolean array, which gives us the number of equal elements.

Note that the solution assumes that the tensors `A` and `B` have the same shape, i.e., they are both of dimension 1000 * 1.