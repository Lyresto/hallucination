# Normalize each column of the sparse matrix
for col in range(sa.shape[1]):
    column = sa[:, col].toarray().flatten()  # Convert the sparse column to a dense array
    column_norm = np.linalg.norm(column)  # Calculate the norm of the column
    sa[:, col] = column / column_norm  # Normalize the column by dividing it by its norm
