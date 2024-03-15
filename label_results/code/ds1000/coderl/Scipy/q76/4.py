import scipy.optimize as scipy
from numpy import dot

def residual(pars, a, y):
	vals = pars.valuesdict()
	x = vals['x']
	model = func(x,a)
	return (y - model)**2

def myfunc():
	a = np.array([ [ 0, 0, 1, 1, 1 ],
				 [ 1, 0, 1, 0, 1 ],
				 [ 0, 1, 0, 1, 0 ] ])
	# true values of x
	x_true = np.array([10, 13, 5, 8, 40])
	# data without noise
	y = func(x_true,a)
	#************************************
	# Apriori x0
	x0 = np.array([2, 3, 1, 4, 20])
	fit_params = Parameters()
	fit_params.add('x', value=x0)
	out = scipy.optimize.minimize(residual, fit_params, args=(a, y))
	print(out)
	# result should be optimal x array
	print(out.x)

myfunc()
