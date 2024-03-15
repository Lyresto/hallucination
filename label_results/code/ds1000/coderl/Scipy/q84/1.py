import scipy.integrate
def f(c=5, low=0, high=1):
	# return the solution in this function
	# result = f(c=5, low=0, high=1)
	# I=[]
	# for n in range(len(c)):
	#     # equation
	#     eqn = 2*x*c[n]
	#     # integrate 
	#     result,error = scipy.integrate.quad(lambda x: eqn,0,1)
	#     I.append(result)
	# I = array(I)
	# return I
	I=[]
	for n in range(len(c)):
		# equation
		eqn = 2*c[n]
		# integrate 
		result,error = integrate.quad(lambda x: eqn,low,high)
		I.append(result)
		I.append(error)
	return I
