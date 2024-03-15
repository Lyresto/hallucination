import numpy as np
import scipy.sparse
lil_sparse_matrix = lil_matrix(np.zeros((10, 10)))

def have_element(i, j):
	return i in lil_sparse_matrix and j in lil_sparse_matrix

lil_sparse.make_symmetric()
# M = scipy.sparse.csr_matrix(np.zeros((10, 10)), dtype=np.int32)
for i, x in enumerate(lil_sparse_matrix):
	if i!= j and have_element(i, j):
		lil_sparse_matrix[i, j] = x
