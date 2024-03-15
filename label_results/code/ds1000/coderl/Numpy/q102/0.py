import numpy as np


def extract_columns(a, low, high):
	return np.array([a[:, i] for i in range(low, high + 1)])
