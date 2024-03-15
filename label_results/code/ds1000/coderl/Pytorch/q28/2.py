from itertools import product
from functools import reduce

def fill_mat(a, lengths):
	return reduce(lambda a, b: a[:, None, b] + b, product(range(len(a)), repeat=len(lengths)), 0)
