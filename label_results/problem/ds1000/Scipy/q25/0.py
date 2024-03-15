# One workaround is to create a new csr_matrix with the diagonal elements removed
# We can do this by creating a new array with the diagonal elements set to 0
# and then using the dia_matrix constructor to create a diagonal matrix
# Finally, we can subtract this diagonal matrix from the original matrix

diagonal = sparse.dia_matrix((np.zeros(2), [0]), shape=(2, 2))
b = b - diagonal
