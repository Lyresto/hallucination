import numpy as np

def extract(a):
	b = np.pad(a, 2, 'constant')
	c = np.pad(b, 2, 'constant')
	return [[np.split(c, k)[::2]] for k in range(len(a))]
