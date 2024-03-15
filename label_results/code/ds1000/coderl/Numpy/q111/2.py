import numpy as np

def sub2ind(n, k, i, j):
	s1 = np.dot(np.arange(n),np.roll(np.arange(n),k))
	s2 = np.dot(np.arange(j),np.roll(np.arange(n),i))
	return (s1-s2).round()
