import numpy as np

def mean(a):
	try:
		return np.mean(a)
	except ValueError as e:
		return np.inf + np.nan * len(a)
