def f(sA=example_sA):
	lil_sparse_matrix = lil_matrix(sA.copy())
	lil_sparse_matrix.make_symmetric()
	return lil_sparse_matrix
