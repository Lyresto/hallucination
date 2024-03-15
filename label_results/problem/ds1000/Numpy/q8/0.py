# Get the unique values in a and sort them
unique_vals = np.sort(np.unique(a))

# Create an empty one-hot array with the correct shape
b = np.zeros((a.size, unique_vals.size), dtype=int)

# Loop over the unique values and set the corresponding one-hot column
for i, val in enumerate(unique_vals):
    b[:, i] = (a == val).ravel().astype(int)

# Reshape b to match the shape of a
b = b.reshape(a.shape[0], a.shape[1], -1, order='F')
