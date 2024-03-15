import numpy as np
import pandas as pd
import torch

a = torch.randn(1, 3, 40, 10, 1)

chunk_dim = 10
step = 1
num_splits = (a.shape[2] - chunk_dim) // step + 1

# Create an empty list to store the split tensors
a_split = []

# Iterate over the range of splits
for i in range(num_splits):
    start_idx = i * step
    end_idx = start_idx + chunk_dim
    
    # Split the tensor along the third dimension
    split_tensor = a[:, :, start_idx:end_idx, :, :]
    
    # Append the split tensor to the list
    a_split.append(split_tensor)

# Verify the number of splits
assert len(a_split) == num_splits

# Print the shapes of the split tensors
for i, split_tensor in enumerate(a_split):
    print(f"Shape of tensor_{i+1}: {split_tensor.shape}")
    print(split_tensor)

# Return the list of split tensors
a_split