from scipy.sparse import csr_matrix


def f(sA: lil_matrix) -> lil_matrix:
	"""
	Make the sparse matrix symmetric.
	"""
	lil_sparse = sA.copy()
	lil_sparse.make_symmetric()
	return lil_sparse
