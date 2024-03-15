import numpy as np
def f(a = example_a, pos=2, element = 66):
	# return the solution in this function
	a_l = a.tolist()
	a_l.insert(pos, element)
	return np.asarray(a_l)
