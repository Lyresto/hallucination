import numpy as np

def extract(a):
	b = np.zeros_like(a)
	c = np.zeros_like(a)
	
	for i in range(len(a)):
		for j in range(len(a[i])):
			b[i, j] = a[i, j] + a[i + 1, j]
			
	for i in range(len(a) - 1):
		for j in range(len(a[i])):
			c[i, j] = a[i][j] + a[i + 1, j]
			
	return b, c
