def csr_matrix(A, copy=True, k=0, verbose=False):
	if copy or k == 0:
		A = A.copy() if copy else A
		A.diag_set(k-1, 0) if verbose else None
	return A
