import numpy as np

def cumulative_sum(a, col, multiply_number):
	return np.cumsum(a[:col]) * multiply_number
