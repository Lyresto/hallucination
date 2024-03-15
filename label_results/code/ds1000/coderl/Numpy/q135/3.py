import numpy as np

def generate(a, m):
	n = len(a)
	b = np.array([int(i) for i in bin(a)[2:].zfill(m)], dtype = np.uint8)
	return np.unpackbits(b)
