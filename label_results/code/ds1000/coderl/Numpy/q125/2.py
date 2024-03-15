import numpy as np

def mean(data, bin_size):
	total = 0
	for i, j in zip(data, data[1:]):
		total += (i + j) / bin_size
	return total

def bin_mean(data, bin_size):
	mean = []
	for i in range(len(data) / bin_size + 1):
		mean.append(mean(np.array(data[:i * bin_size]), bin_size))
	return mean
