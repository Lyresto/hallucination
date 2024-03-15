import numpy as np

def shift(xs, shift):
	shifts = (shift[0],) + shift[1:]
	return np.roll(xs, shifts, axis=0)
