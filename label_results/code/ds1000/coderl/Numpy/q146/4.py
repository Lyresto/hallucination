import numpy as np
a = np.array([[0, 1], [2, 1], [4, 8]])
mask = np.array([[True, False], [False, True], [True, False]])


def mask_arrays(a, mask):
	return np.ma.masked_equal(a, np.array(mask))
