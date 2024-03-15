from numpy import concatenate

def f(X):
	return [list(concatenate([a, X], axis=0)) for a in X]
