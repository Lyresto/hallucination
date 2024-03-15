from numpy import numpy as np
def generate(a, m):
	w = np.array([int(np.bin(num)[2:].zfill(m)) for num in a], dtype="int")
	return np.unpackbits(w)
