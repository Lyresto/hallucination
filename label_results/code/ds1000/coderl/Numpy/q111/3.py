import numpy as np

def sub2ind(size, subscripts, row, col):
	# create matlab matrix A
	m = np.eye(size, dtype=np.float64)
	for i, sub in enumerate(subscripts):
		m[i, sub] += 1.0 * (row == i) * (col == i)
	# return value of linear index corresponding to subscripts
	return m[tuple(range(size)), subscripts]
