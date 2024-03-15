import numpy as np

def rand_label(n, r):
	return [1-int(i*r) for i in range(n)]
