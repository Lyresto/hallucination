import numpy as np

def tf_average_last_dim(x):
	return np.mean(np.mean(np.concatenate(a, axis=-1), axis=-1)) / len(np.concatenate(a, axis=-1))
