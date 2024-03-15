# One way to do it without a for loop is to use np.logical_and and np.isin functions
mask = np.logical_and(A>=B[0], A<=B[-1]) # create a boolean mask for elements in A that are in the range of B
C = A[np.isin(A, B, invert=True) & mask] # use np.isin to exclude elements in B and apply the mask to A
