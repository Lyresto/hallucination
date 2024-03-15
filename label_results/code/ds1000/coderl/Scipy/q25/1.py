# Attempt to detect `-1` and `0` diagonal elements on the sparse matrix

# Convert to CSR format
# >>> a = np.ones((2,2))
# >>> c = sparse.csr_matrix(a)
# >>> c.setdiag(0)
# >>> c
# <2x2 sparse matrix of type '<type 'numpy.float64'>'
#     with 2 stored elements in Compressed Sparse Row format>

# Convert to LIL format
# >>> a = np.ones((2,2))
# >>> b = sparse.lil_matrix(a)
# >>> b.setdiag(0)
# >>> b
# <2x2 sparse matrix of type '<type 'numpy.float64'>'
#     with 2 stored elements in LInked List format>

# Change diagonal to specified value
# >>> b.setdiag(1)
# >>> b
# <2x2 sparse matrix of type '<type 'numpy.float64'>'
#     with 2 stored elements in Compressed Sparse Row format>
