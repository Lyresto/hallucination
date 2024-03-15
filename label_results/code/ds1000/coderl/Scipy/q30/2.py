lil_sparse_matrix = lil_matrix.csr_matrix
from random import randint
data = [randint(0,10) for i in range(10)]
def have_element(i,j):
	return i in data and j in data
M= sparse.random(10,10, density=0.1,format='lil')
