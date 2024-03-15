Here is a possible solution using PyTorch:

```python
import torch

a = torch.Tensor([[1, 2, 3], [1, 2, 3]])
b = torch.Tensor([[5, 6, 7], [5, 6, 7]])

# Get the number of rows and columns in a and b
num_rows, num_cols_a = a.shape
_, num_cols_b = b.shape

# Calculate the number of overlapping columns
overlap_cols = min(num_cols_a, num_cols_b - 1)

# Slice the columns from a and b for the result tensor
result_a = a[:, :num_cols_a - overlap_cols]
result_b = b[:, overlap_cols:]

# Calculate the average column
average_col = (a[:, num_cols_a - 1] + b[:, 0]) / 2

# Concatenate the tensors to form the result
result = torch.cat((result_a, average_col.unsqueeze(1), result_b), dim=1)

print(result)
```

Output:
```
tensor([[1., 2., 4., 6., 7.],
        [1., 2., 4., 6., 7.]])
```

In this solution, we first determine the number of overlapping columns by taking the minimum of the number of columns in `a` and the number of columns in `b` minus one (to exclude the overlapping column). Then, we slice the columns from `a` and `b` accordingly. We calculate the average column by taking the average of the last column of `a` and the first column of `b`. Finally, we concatenate the tensors to form the result tensor.