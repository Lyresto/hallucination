import numpy as np
Z = np.random.rand(*np.random.randint(2, 10, (np.random.randint(2, 10))))
ans = np.zeros_like(Z)

def slicing(Z):
	#...
	ans[:] = Z[:]
	if Z.ndim == 1:
		return Z[0]
	if Z.ndim == 2:
		return Z[:,0]
	return Z[:,:,0]
