from numpy import concatenate

def f(X):
	return list(concatenate(X, axis=0))
