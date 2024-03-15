import numpy as np
import scipy.interpolate

# create an array to interpolate over the 1st axes
def create_array():
	array = np.random.randint(0, 9, size=(100, 100, 100))
	x = np.arange(0, 100, 1)
	y = np.arange(0, 100, 0.1)
	new_array = np.zeros((1000, 100, 100))
	for i in x:
		for j in x:
			f = scipy.interpolate.interp1d(x, array[:, i, j])
			new_array[:, i, j] = f(y)
	
	return new_array
