To slice a PyTorch tensor using a logical index on the columns, you can use the `torch.masked_select()` function. Here's how you can modify your code to achieve the desired result:

```python
import torch

C = torch.LongTensor([[1, 3], [4, 6]])
# 1 3
# 4 6

A_log = torch.ByteTensor([1, 0, 1]) # the logical index
B = torch.LongTensor([[1, 2, 3], [4, 5, 6]])

# Create a mask tensor from the logical index
mask = A_log.unsqueeze(0).expand(B.size())

# Use masked_select to select the columns based on the mask
C = torch.masked_select(B, mask)

# Reshape the result to match the desired output shape
C = C.view(B.size(0), -1)

print(C)
```

Output:
```
tensor([[1, 3],
        [4, 6]])
```

In this solution, we first create a mask tensor by expanding the logical index `A_log` to match the size of tensor `B`. Then, we use `torch.masked_select()` to select the elements from `B` based on the mask. Finally, we reshape the result to match the desired output shape.

Note that the `unsqueeze(0)` and `view()` operations are used to manipulate the dimensions of the tensors to ensure they can be broadcasted correctly.