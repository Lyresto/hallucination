import numpy as np
def hyp(x):
	return x**2 + x*x + (x**4 - x*x)

def solve(x, y):
	r = np.array([hyp(i) for i in x])
	z = np.array([hyp(j) for j in y])
	w = z - r
	return [w.argmin(), w.min(), w.max()]
