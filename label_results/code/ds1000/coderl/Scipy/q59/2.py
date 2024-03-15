#!/usr/bin/env python3

import numpy as np
from scipy.sparse import csr_matrix

def get_array(matrix, row_idx, col_idx):
	arr = np.array(matrix[row_idx])
	return arr[col_idx]

def get_row(matrix, row_idx):
	return matrix[row_idx]

def get_column(matrix, col_idx):
	return matrix[:,col_idx]

def solve():
	matrix = csr_matrix((get_array(matrix, r, c), (row, col)) for row in range(len(matrix)) for col in range(len(matrix[row])))
	return get_row(matrix).tolist()

solve()
