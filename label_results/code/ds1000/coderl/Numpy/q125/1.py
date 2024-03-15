import numpy as np

def mean(data, bin_size):
	return np.mean(np.concatenate((np.split(data, bin_size), np.split(data, -bin_size)), axis = 0))
