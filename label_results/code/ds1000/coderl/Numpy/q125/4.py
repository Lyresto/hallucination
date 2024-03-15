import numpy as np

def mean(arr, size): 
	n = len(arr) 
	return np.mean(np.array(arr).reshape(n, size)).tolist()

def mean_bin(data, size):
	return [mean(arr, size) for arr in data]
