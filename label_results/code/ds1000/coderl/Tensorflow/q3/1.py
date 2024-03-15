import numpy as np


def accuracy(labels, result):
	return np.sum(result) / np.sum(labels)
