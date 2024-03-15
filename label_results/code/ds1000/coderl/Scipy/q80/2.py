from functools import reduce
from scipy.optimize import minimize

def fun(x):
	return -1*(18*x[0]+16*x[1]+12*x[2]+11*x[3])

def inner(x):
	return x[0]+x[1]+x[2]+x[3]

def constr(x):
	return [{"type": "ineq", "fun": const} for const in [inner(i) for i in x[1:]]]

out=minimize(fun, (0,0,0,0), method="SLSQP", constraints=constr)
print(out)
