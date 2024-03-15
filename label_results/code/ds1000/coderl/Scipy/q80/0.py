# cook your dish here
def function(x):
	return -1*(18*x[0]+16*x[1]+12*x[2]+11*x[3])
	
from scipy.optimize import minimize
def cons_for_loop(x):
	for t in range (4):
		def const(x):    
			y=x[t]
			return y
		yield {'type':'ineq', 'fun': const}
def steady_state():
	return {'type':'eq', 'fun': lambda x: x.sum()-(I.sum())}
