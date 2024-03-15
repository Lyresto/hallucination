You can use the `torch.eq()` function to check for element-wise equality between two tensors. Then, you can use the `torch.sum()` function to count the number of elements that are equal.

Here's an example of how you can implement this:

```python
import torch

def count_equal_elements(A, B):
    # Check for element-wise equality
    equal_elements = torch.eq(A, B)
    
    # Count the number of equal elements
    count = torch.sum(equal_elements).item()
    
    return count
```

In this example, `A` and `B` are the input tensors of dimension 1000 * 1. The `torch.eq()` function returns a tensor of the same shape as the input tensors, where each element is `True` if the corresponding elements in `A` and `B` are equal, and `False` otherwise. Then, the `torch.sum()` function is used to sum all the `True` values in the `equal_elements` tensor, and the `.item()` method is used to convert the resulting tensor to a Python integer.

You can use this function as follows:

```python
A, B = load_data()  # Load your tensors here
cnt_equal = count_equal_elements(A, B)
print("Number of equal elements:", cnt_equal)
```

Make sure to replace the `load_data()` function with the appropriate code to load your tensors.