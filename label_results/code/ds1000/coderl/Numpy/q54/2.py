import numpy as np

# def multiply_column_by_number(array, col, multiply_number):
#     return np.multiply(array[:col], multiply_number)

def cumulative_sum(array, col):
	return np.cumsum(array[:col])
