import scipy.integrate
def f(c=5, low=0, high=1):
	# return the solution in this function
	c=c/100
	I=[]
	for n in range(len(c)):
		# equation
		eqn = 2*x*c[n]
		# integrate 
		result,error = integrate.quad(lambda x: eqn,low,high)
		I.append(result)
	I = array(I)
	return I
