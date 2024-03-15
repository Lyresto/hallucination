import numpy as np


def f(lengths=example_lengths):
	L = np.array(lengths)
	return np.pad(L, 1, mode="constant").reshape(8, 8)
