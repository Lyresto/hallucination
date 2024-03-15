To slice a PyTorch tensor using a logical index on the columns, you can use the `torch.masked_select()` function. Here's how you can modify your code to achieve this:

```python
import torch

C = torch.LongTensor([[1, 3], [4, 6]])
# 1 3
# 4 6

A_log = torch.ByteTensor([1, 0, 1])  # the logical index
B = torch.LongTensor([[1, 2, 3], [4, 5, 6]])

# Convert the logical index to a Boolean mask
mask = A_log.byte()

# Apply the mask to the columns of B using masked_select()
C = B[:, mask]

print(C)
```

Output:
```
tensor([[1, 3],
        [4, 6]])
```

By converting the logical index tensor `A_log` to a Boolean mask using `A_log.byte()`, we can then apply the mask to the columns of `B` using `B[:, mask]`. This will select the columns of `B` where the corresponding values in `A_log` are `True`.