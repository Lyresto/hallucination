# Get the number of rows in the tensors
num_rows = a.shape[0]

# Create a new tensor with the desired shape
result = torch.zeros((num_rows, a.shape[1] + b.shape[1] - 1))

# Copy the first two columns of 'a' into the result tensor
result[:, :2] = a[:, :2]

# Calculate the average of the last column of 'a' and the first column of 'b'
avg = (a[:, 2] + b[:, 0]) / 2

# Copy the average column into the result tensor
result[:, 2] = avg

# Copy the last two columns of 'b' into the result tensor
result[:, 3:] = b[:, 1:]

return result
### END SOLUTION