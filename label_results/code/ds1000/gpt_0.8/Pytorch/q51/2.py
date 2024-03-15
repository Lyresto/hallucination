Here's one way to solve the problem using PyTorch:

```python
import torch

def count_equal_elements(A, B):
    # Convert A and B to PyTorch tensors if they are not already
    if not isinstance(A, torch.Tensor):
        A = torch.tensor(A)
    if not isinstance(B, torch.Tensor):
        B = torch.tensor(B)
    
    # Ensure that A and B have the same shape
    assert A.shape == B.shape, "A and B must have the same shape"
    
    # Count the number of equal elements
    cnt_equal = torch.sum(A == B)
    
    return cnt_equal
```

You can use this function as follows:

```python
A, B = load_data()
cnt_equal = count_equal_elements(A, B)
print(cnt_equal)
```

Note that this function assumes that `A` and `B` are either PyTorch tensors or arrays that can be converted to tensors. If they are not, you may need to modify the code accordingly.