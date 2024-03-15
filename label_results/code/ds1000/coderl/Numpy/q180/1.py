import numpy as np
def rsl(z):
	a = np.array(z)
	k = len(a)
	return a[k//2:,k//2:-1,-1:-1].reshape(k,-1)
