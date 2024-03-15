import numpy as np
import torch

def solve(A_log, B):
	# return the solution in this function
	C = B[:, A_log]
	# C = B[A_log]
	return C[A_log]

def load_data():
	a, b = np.array(list(zip(*pd.read_csv('data/wolf/wolf_1.csv').values())), np.array(list(zip(*pd.read_csv('data/wolf/wolf_2.csv').values())))
	a = a.view(-1, len(b))
	b = b.view(-1, len(a))
	return [a, b]
