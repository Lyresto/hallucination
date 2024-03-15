import numpy as np
a = np.array([[0, 3, 1, 3], [3, 0, 0, 0], [1, 0, 0, 0], [3, 0, 0, 0]])
# a = np.array([[0, 3, 1, 3], [3, 0, 0, 0], [1, 0, 0, 0], [3, 0, 0, 0]])
zero_column, zero_row = 0, 0

def zero_out(a):
	for r in range(len(a)):
		if a[r][0] == zero_row:
			a[r][zero_row] = 0
		elif a[r][zero_col] == zero_column:
			a[r][zero_col] = 0
