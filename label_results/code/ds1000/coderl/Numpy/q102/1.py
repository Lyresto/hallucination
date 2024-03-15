import numpy as np


def extract_columns(a, low=1, high=10):
	r = []
	
	while low <= len(a) - high:
		c = a[:][low - 1:high]
		r.append(list(c[low - 1:high]))
		low += 1
	
	return r
