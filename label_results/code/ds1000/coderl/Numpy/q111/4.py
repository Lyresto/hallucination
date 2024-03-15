import numpy as np
def sub2ind(n, k, i, j):
	s = np.arange(n)[i::k+1].reshape(n,-1).tolist()
	return s[j]
