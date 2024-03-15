To solve this problem, you can use the torch.cat() function to concatenate the tensors along the second dimension (columns). Then, you can use the torch.mean() function to calculate the average of the overlapping elements.

Here's the code to solve the problem:

```python
import torch

a = torch.Tensor([[1, 2, 3], [1, 2, 3]])
b = torch.Tensor([[5, 6, 7], [5, 6, 7]])

def solve(a, b):
    overlap = (a[:, -1] + b[:, 0]) / 2
    result = torch.cat((a[:, :-1], overlap.unsqueeze(1), b[:, 1:]), dim=1)
    return result

result = solve(a, b)
print(result)
```

Output:
```
tensor([[1., 2., 4., 6., 7.],
        [1., 2., 4., 6., 7.]])
```

In this solution, we first calculate the average of the overlapping elements by adding the last column of `a` and the first column of `b`, and then dividing it by 2. We use the `.unsqueeze(1)` function to add an extra dimension to the overlap tensor, so that it can be concatenated with `a` and `b`.

Finally, we concatenate `a[:, :-1]` (all columns of `a` except the last one), `overlap`, and `b[:, 1:]` (all columns of `b` except the first one) along the second dimension using the `torch.cat()` function. The resulting tensor is returned as the solution.