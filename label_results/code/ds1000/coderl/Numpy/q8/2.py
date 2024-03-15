import numpy as np

def gen(a):
	for row in a:
		for i, v in enumerate(row):
			yield i, v

def get_indexes(a):
	return np.argwhere(a).T
