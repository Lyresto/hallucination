import numpy as np
a = np.random.rand(8, 5)
col = 2
multiply_number = 5.2
result =... # put solution in this variable
def cumulative_sum(col):
	return np.cumsum(a[:col])[1:]
