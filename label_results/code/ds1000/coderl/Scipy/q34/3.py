from scipy.sparse import csr_matrix

# I can see that the standard deviation is very weak.
# I considered the way to standardize the matrix to make it more obvious and
# approximately good for linear analysis.

# Using the mean and standard deviation from the csr_matrix construction helps you
# understand better quantities.

mean, standard_deviation = csr_matrix(np.mean(arr)).mean(), csr_matrix(np.std(arr)).std()
