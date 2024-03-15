import numpy as np
import torch
A_log, B = load_data()
def solve(A_log, B):
	# return the solution in this function
	# C = solve(A_log, B)
	C = B[:, A_log]
	# logical indexing on the columns only:
	for i, value in enumerate(A_log):
		C[i] = value
	return C
