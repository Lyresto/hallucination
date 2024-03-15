One way to solve this problem is to use the `torch.eq` function to compare the two tensors element-wise, and then use the `torch.sum` function to count the number of equal elements.

Here's one possible solution:

```python
import torch

def Count(A, B):
    equal_elements = torch.eq(A, B)
    cnt_equal = torch.sum(equal_elements)
    return cnt_equal.item()
```

In this solution, the `torch.eq` function compares the elements of tensors `A` and `B` element-wise and returns a new tensor of the same shape where each element is `True` if the corresponding elements in `A` and `B` are equal, and `False` otherwise.

The `torch.sum` function is then used to calculate the sum of all the `True` values in the `equal_elements` tensor, which gives the count of equal elements.

Finally, the `.item()` method is used to extract the count as a Python scalar.

You can then call this function with your tensors `A` and `B` to get the count of equal elements:

```python
cnt_equal = Count(A, B)
print(cnt_equal)
```

Note that this solution assumes that the tensors `A` and `B` have the same shape, i.e., both have dimensions 1000 * 1.