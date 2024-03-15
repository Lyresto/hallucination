import numpy as np

def matrix_to_array(a, m):
	return np.unpackbits(np.array(a, dtype=np.uint8)).reshape(len(a), m)
