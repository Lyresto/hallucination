def f(sA = example_sA, sB = example_sB):
	# return the solution in this function
	# result = f(sA, sB)
	# sp.sparse.csr_matrix(np.array([[1,2,3],[4,5,6],[7,8,9]])) * sp.sparse.csr_matrix(np.array([0,1,2]))
	return np.array([[1,2,3],[4,5,6],[7,8,9]]) * sA + np.array([0,1,2]) * sB
