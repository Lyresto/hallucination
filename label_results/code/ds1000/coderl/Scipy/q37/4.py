import numpy as np
def fit_fourier(f,x,y):
	a1,a2 = f(x,*y[:4])
	return [a1,a2]
def point_of_fit(a1,a2):
	return (a1,a2)
def two_point_fit(a1,a2):
	return (a2,a1)
def fourier1(x,a1):
	return a1 * np.cos(1 * np.pi / x)
def fourier2(x,a1,a2):
	return a1 * np.cos(2 * np.pi / x)
def fourier3(x,a1,a2,a3):
	return a1 * np.cos(3 * np.pi / x)
def fourier4(x,a1,a2,a3,a4):
	return a1 * np.cos(4 * np.pi / x)
def fourier5(x,a1,a2,a3,a4,a5,a6,a7,a8):
	return a1 * np.cos(5 * np.pi / x) + a2 * np.cos(6 * np.pi / x) + a3 * np.cos(7 * np.pi / x) + a4 * np.cos(8 * np.pi / x)
def fourier6(x,a1,a2,a3,a4,a5,a6,a7,a8):
	return a1 * np.cos(6 * np.pi / x) + a2 * np.cos(7 * np.pi / x) + a3 * np.cos(8 * np.pi / x)
def fourier7(x,a1,a2,a3,a4,a5,a6,a7,a8):
	return a1 * np.cos(7 * np.pi / x) + a2 * np.cos(8 * np.pi / x) + a3 * np.cos(9 * np.pi / x) + a4 * np.cos(10 * np.pi / x)
def fourier8