import numpy as np
import math
def fourier8(x, a1, a2, a3, a4, a5, a6, a7, a8):
	return a1 * np.cos(1 * np.pi / tau * x) + \
           a2 * np.cos(2 * np.pi / tau * x) + \
           a3 * np.cos(3 * np.pi / tau * x) + \
           a4 * np.cos(4 * np.pi / tau * x) + \
           a5 * np.cos(5 * np.pi / tau * x) + \
           a6 * np.cos(6 * np.pi / tau * x) + \
           a7 * np.cos(7 * np.pi / tau * x) + \
           a8 * np.cos(8 * np.pi / tau * x)

def fun(x,a1):
	return a1 * np.cos(1 * np.pi / tau * x)

popt, pcov = curve_fit(fun, np.array([1,2,3,4,5,6,7,8]),np.array([0.045,0.001,1,2,3,4,5,6,7,8]))
print(popt)
