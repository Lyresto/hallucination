import numpy as np
def divide_by_n_zeros(x):
	weights = x[0][0][0]
	sum_of_zeros = 0
	for i in range(len(x[0][0])):
		if x[0][0][i]!= 0:
			sum_of_zeros += 1
	# print(sum_of_zeros)
	for i in range(len(x[0][0])):
		weights += x[0][0][i]
	# print(weights)
	return weights / sum_of_zeros
