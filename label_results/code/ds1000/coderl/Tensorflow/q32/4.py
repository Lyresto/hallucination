import numpy as np

def mean(x):
	return np.mean(np.array(x, dtype=np.float64), axis=-1)
