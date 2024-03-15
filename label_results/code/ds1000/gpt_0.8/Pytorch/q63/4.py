One way to solve this problem is by using NumPy to manipulate the tensors. Here's one possible implementation:

```python
import numpy as np

def solve(a, b):
    # Check if the tensors have the same number of rows
    assert a.shape[0] == b.shape[0], "Tensors must have the same number of rows"

    # Get the number of rows and columns in 'a' and 'b'
    num_rows = a.shape[0]
    num_cols_a = a.shape[1]
    num_cols_b = b.shape[1]

    # Create an empty tensor to store the result
    result = np.zeros((num_rows, num_cols_a + num_cols_b - 1))

    # Copy the first part of 'a' into the result
    result[:, :num_cols_a] = a

    # Compute the average of the overlapping columns
    overlap_avg = (a[:, -1] + b[:, 0]) / 2

    # Copy the overlapping average into the result
    result[:, num_cols_a-1:num_cols_a+1] = overlap_avg[:, np.newaxis]

    # Copy the last part of 'b' into the result
    result[:, num_cols_a:] = b[:, 1:]

    return result

# Test the function
a = np.array([[1, 2, 3], [1, 2, 3]])
b = np.array([[5, 6, 7], [5, 6, 7]])
result = solve(a, b)

print(result)
```

Output:
```
[[1. 2. 4. 6. 7.]
 [1. 2. 4. 6. 7.]]
```

This implementation creates an empty tensor `result` with the appropriate dimensions. It then copies the first part of `a` into the result, computes the average of the overlapping columns, and copies the last part of `b` into the result. Finally, it returns the result tensor.

Note that the result tensor is created using NumPy, as PyTorch does not support direct manipulation of tensor dimensions in the same way. If you need to convert the result tensor back to a PyTorch tensor, you can use `torch.from_numpy(result)`.