import scipy.integrate
def f(c=5, low=0, high=1):
	i=0
	n=len(c)
	for n in range(n):
		eqn=2*c[n]*c[n]
		result,error=scipy.integrate.quad(lambda x: eqn,low,high)
		i+=result
	return i
