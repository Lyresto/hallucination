Here's a possible solution to batch convert sentence lengths to masks in PyTorch:

```python
import torch

lens = [3, 5, 4]

# Calculate the maximum length of the sentences
max_len = max(lens)

# Create an empty mask tensor with shape (batch_size, max_len)
mask = torch.zeros(len(lens), max_len, dtype=torch.long)

# Iterate over each sentence length and set the corresponding mask values
for i, length in enumerate(lens):
    mask[i, :length] = 1

# Print the result
print(mask)
```

This will output:

```
tensor([[1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0]])
```

Note that this solution assumes that you have already loaded the sentence lengths into the `lens` variable. You can replace `lens = [3, 5, 4]` with your own data loading code.