# Convert the sparse matrix to csr format
sa = sa.tocsr()

# Iterate through each column of the matrix
for col in range(sa.shape[1]):
    # Get the column as a numpy array
    column = sa[:, col].toarray().flatten()

    # Normalize the column
    norm = np.linalg.norm(column)
    column_normalized = column / norm

    # Update the original column in the matrix
    sa[:, col] = column_normalized.reshape((-1, 1))

