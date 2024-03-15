import numpy as np
import scipy.interpolate

def array_interpolate(a, b):
	return np.interp(a, b, a)
