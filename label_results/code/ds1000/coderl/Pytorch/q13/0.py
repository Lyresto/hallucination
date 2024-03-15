import numpy as np
import torch
A_log, B = load_data()
def solve(A_log, B):
	# return the solution in this function
	# C = solve(A_log, B)
	### BEGIN SOLUTION
	C = B[:, A_log]
	return C
