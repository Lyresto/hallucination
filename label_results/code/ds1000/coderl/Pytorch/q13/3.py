import numpy as np
import torch
def solve(A_log, B):
	# return the solution in this function
	C = B[:, A_log]
	return C[A_log]

