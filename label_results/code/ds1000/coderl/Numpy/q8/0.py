import numpy as np

def one_hot(i, a):
	c = np.ones((2*i+1, 2*i+1), dtype=np.int)
	for j in range(i):
		c[j+1, a[j,0]] = 1
	return c.astype(np.int)

def encode_as_1_hot(i, a):
	c = np.zeros((2*i+1, 2*i+1), dtype=np.int)
	for j in range(i):
		c[j+1, a[j,0]] = 1
	return c
