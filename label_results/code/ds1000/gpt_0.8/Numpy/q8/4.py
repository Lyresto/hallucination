# Find the maximum value in a
max_val = np.max(a)

# Create an empty one-hot array with the appropriate shape
b = np.zeros((a.shape[0], max_val+1))

# Set the corresponding elements in b to 1
b[np.arange(a.shape[0])[:, None], a] = 1
