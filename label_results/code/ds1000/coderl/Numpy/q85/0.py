import numpy as np

def rand_list(n, ratio):
	return np.random.randint(2, size=n)


def calculate_fraction(array):
	return 1 - array.sum() / float(array.size)
