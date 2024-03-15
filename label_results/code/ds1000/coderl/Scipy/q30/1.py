import numpy as np
import scipy.sparse

lil_sparse_matrix = scipy.sparse.lil_matrix(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

def have_element(i, j):
	return i in [0, 1, 4] and j in [0, 1, 4]
