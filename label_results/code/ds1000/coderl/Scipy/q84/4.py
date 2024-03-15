import scipy.integrate
def f(c=5, low=0, high=1):
	# return the solution in this function
	# result = f(c=5, low=0, high=1)
	i=0
	while i<len(c):
		eqn=2*c[i]*c[i]
		result,error = integrate.quad(lambda x: eqn,low,high)
		I.append(result)
		i += 1
	I = array(I)
	return I
