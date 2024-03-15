To slice a PyTorch tensor using a logical index on the columns, you can convert the logical index tensor to a boolean mask and then use the mask for indexing.

Here's how you can modify your code to achieve this:

```python
import torch

C = torch.LongTensor([[1, 3], [4, 6]])
# 1 3
# 4 6

A_log = torch.ByteTensor([1, 0, 1]) # the logical index
B = torch.LongTensor([[1, 2, 3], [4, 5, 6]])

# Convert the logical index tensor to a boolean mask
mask = A_log.bool()

# Use the boolean mask for indexing
C = B[:, mask]

print(C)
```

This will give you the desired output:

```
tensor([[1, 3],
        [4, 6]])
```

Note that the `bool()` function is used to convert the `torch.ByteTensor` to a boolean mask.