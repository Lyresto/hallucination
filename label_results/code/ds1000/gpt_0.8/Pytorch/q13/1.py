To slice a PyTorch tensor using a logical index on the columns, you can use the `torch.masked_select()` function. Here's how you can modify your code to achieve that:

```python
import torch

C = torch.LongTensor([[1, 3], [4, 6]])
# 1 3
# 4 6

A_log = torch.ByteTensor([1, 0, 1]) # the logical index
B = torch.LongTensor([[1, 2, 3], [4, 5, 6]])

C = B[:, torch.nonzero(A_log).squeeze()] # use torch.nonzero() to get the indices of non-zero elements in A_log
print(C)
```

Output:
```
tensor([[1, 3],
        [4, 6]])
```

In this code, `torch.nonzero(A_log)` returns the indices of non-zero elements in `A_log`. The `squeeze()` function is used to remove any extra dimensions. Finally, these indices are used to slice the tensor `B` to get the desired columns.

Note: `torch.masked_select()` can also be used in this scenario, but it requires converting `A_log` to a `torch.BoolTensor` instead of `torch.ByteTensor`.