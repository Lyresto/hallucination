# Iterate through columns
for col in range(sa.shape[1]):
    # Get the column as a dense array
    column = sa[:, col].toarray().flatten()
    
    # Normalize the column
    norm = np.linalg.norm(column)
    normalized_column = column / norm
    
    # Update the column in the sparse matrix
    sa[:, col] = normalized_column.reshape(-1, 1)
    
END SOLUTION