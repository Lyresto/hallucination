import numpy as np

def f(a = example_a, pos=2, element = 66):
	# return the solution in this function
	# a = f(a, pos=2, element = 66)
	arr = np.array(a)
	arr.insert(pos, element)
	return arr
