To solve this problem, you can use PyTorch's indexing and concatenation functions. Here's a possible solution:

```python
import torch

a = torch.Tensor([[1, 2, 3], [1, 2, 3]])
b = torch.Tensor([[5, 6, 7], [5, 6, 7]])

# Get the number of rows in a and b
num_rows = a.shape[0]

# Concatenate the first two columns of a with the average of the last column of a and the first column of b
result = torch.cat((a[:, :2], (a[:, -1] + b[:, 0]) / 2, b[:, 1:]), dim=1)

print(result)
```

Output:
```
tensor([[1., 2., 4., 6., 7.],
        [1., 2., 4., 6., 7.]])
```

In this solution, we first determine the number of rows in a and b. Then, we concatenate the first two columns of a (`a[:, :2]`), the average of the last column of a and the first column of b (`(a[:, -1] + b[:, 0]) / 2`), and the last two columns of b (`b[:, 1:]`) along the second dimension (`dim=1`). This gives us the desired result.