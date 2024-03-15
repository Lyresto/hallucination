import numpy as np

def fit_fourier(f, x, y):
	a1, a2 = f(x, *y[:2])
	return (a1, a2)

def first_fourier(x, a1):
	return a1 * np.cos(1 * np.pi / x)

def second_fourier(x, a2, a3):
	return a2 * np.cos(2 * np.pi / x) + a3 * np.cos(3 * np.pi / x)

def third_fourier(x, a4, a5, a6, a7, a8):
	return a4 * np.cos(4 * np.pi / x) + a5 * np.cos(5 * np.pi / x) + a6 * np.cos(6 * np.pi / x) + a7 * np.cos(7 * np.pi / x) + a8 * np.cos(8 * np.pi / x)

def fourier1(x, a1):
	return a1 * np.cos(1 * np.pi / x)

def fourier2(x, a2, a3, a4, a5, a6, a7, a8):
	return a2 * np.cos(2 * np.pi / x) + a3 * np.cos(3 * np.pi / x) + a4 * np.cos(4 * np.pi / x) + a5 * np.cos(5 * np.pi / x) + a6 * np.cos(6 * np.pi / x) + a7 * np.cos(7 * np.pi / x) + a8 * np.cos(8 * np.pi / x)

def fourier3(x, a1, a2, a3, a4, a5, a6, a7, a8):
	return a1 * np.cos(1 * np.pi / x) + a2 * np.cos(2 * np.pi / x) + a3 * np.cos(3 * np.pi / x) + a4 * np.cos(4 * np.pi / x) +