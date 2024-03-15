import scipy.optimize
import numpy as np
np.random.seed(42)
a = np.random.rand(3,5)
x_true = np.array([10, 13, 5, 8, 40])
y = a.dot(x_true ** 2)
def residual(pars, a, y):
	vals = pars.valuesdict()
	x = vals['x']
	model = func(x,a)
	return (y - model) ** 2
def func(x,a):
	return np.dot(a, x**2)

min_x = np.array([2, 3, 1, 4, 20])
max_x = np.array([9, 16, 7, 8, 20])
def get_min(min_x, max_x):
	res = scipy.optimize.minimize(residual, dict(x=min_x, y=max_x), method='L-BFGS-B')
	return res.x
def get_max(min_x, max_x):
	res = scipy.optimize.minimize(residual, dict(x=min_x, y=max_x), method='L-BFGS-B')
	return res.x


print(get_min(min_x, max_x))
