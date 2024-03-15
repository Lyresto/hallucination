import numpy as np
from copy import deepcopy

def deep_copy_arrays(arrays):
	return np.array(arrays, copy=True)
