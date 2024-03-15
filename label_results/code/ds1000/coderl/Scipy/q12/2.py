import numpy as np

def f(sA=example_sA, sB=example_sB):
	# return the solution in this function
	return np.dot(sA.todense(), sB.todense())
