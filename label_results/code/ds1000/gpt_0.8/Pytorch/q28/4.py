# Find the maximum length in the lengths tensor
max_length = torch.max(lengths)

# Create a mask tensor with the same shape as 'a'
mask = torch.ones_like(a)

# Set all values after the maximum length to 0 in the mask tensor
mask[:, max_length:] = 0

# Apply the mask tensor to the 'a' tensor
a = a * mask
