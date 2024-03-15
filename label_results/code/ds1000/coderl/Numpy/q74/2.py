import numpy as np
def f(a = example_a, pos=2, element = 66):
	# return the solution in this function
	# a = f(a, pos=2, element = 66)
	list_a = a.copy()
	list_a.insert(pos, element)
	return np.asarray(list_a)
