Here is a solution using PyTorch:

```python
import torch

def Count(A, B):
    assert A.shape == B.shape, "Input tensors must have the same shape"
    
    # Convert tensors to PyTorch tensors if they are not already
    A = torch.tensor(A)
    B = torch.tensor(B)
    
    # Count the number of equal elements
    cnt_equal = torch.sum(A == B)
    
    return cnt_equal
```

In this solution, we first assert that the input tensors have the same shape. Then, we convert the input tensors to PyTorch tensors using `torch.tensor()` if they are not already. Finally, we use the `==` operator to compare the elements of the two tensors element-wise, and then use `torch.sum()` to count the number of equal elements.