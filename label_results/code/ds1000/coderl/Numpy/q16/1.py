import numpy as np

def shift(xs, shift):
	n = len(xs)
	shift = [shift[0], shift[1]]
	out = np.zeros(n, dtype=xs.dtype)
	for i in range(n):
		out[i] = np.roll(xs[i], shift)
	return out
