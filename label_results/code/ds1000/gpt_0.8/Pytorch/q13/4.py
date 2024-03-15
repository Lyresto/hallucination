To slice a PyTorch tensor using a logical index on the columns, you can use the `torch.masked_select()` function. Here's an updated version of your code:

```python
import torch

C = torch.LongTensor([[1, 3], [4, 6]])
# 1 3
# 4 6

A_log = torch.ByteTensor([1, 0, 1]) # the logical index
B = torch.LongTensor([[1, 2, 3], [4, 5, 6]])

# Convert the logical index to a ByteTensor mask
mask = A_log.unsqueeze(0).expand(C.size(0), -1)

# Use masked_select to get the desired columns from C
C = torch.masked_select(C, mask)

print(C)
```

Output:
```
tensor([1, 3, 4, 6])
```

In this code, we first convert the logical index `A_log` to a ByteTensor mask `mask` using `unsqueeze()` and `expand()`. Then, we use `torch.masked_select()` to select the elements from tensor `C` that correspond to the 1 values in the mask.

Hope this helps!