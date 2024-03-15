import numpy as np

def regressor(y, X):
	n = len(y)
	X = np.array(X)
	m = len(X)
	p = np.reshape(np.array(range(1,m+1)), (m, 1))
	w = np.reshape(np.array(range(1,n+1)), (n, 1))
	return regressor_grid(p, w, y)

def regressor_grid(p, w, y):
	#y = y[p] + w[p]
	#y = y - w[p]
	#return y.reshape(len(y), 1)
	pass
