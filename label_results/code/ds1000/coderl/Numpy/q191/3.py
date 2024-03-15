import numpy as np

def solve2(x, y):
	def f(x):
		return x * x + x ** 2
	
	def hyp(x, y):
		res = f(x)
		for i,v in enumerate(y):
			res = min(res, f(v) - v)
		return res
	
	res = np.min(list(zip(y,x)), key=hyp, default=np.inf)
	return [res[0], res[1], res[2]]
	
def solve3(x, y):
	def f(x):
		return x * x + x ** 2
	
	def hyp(x, y):
		res = f(x)
		for i,v in enumerate(y):
			res = min(res, f(v) - v)
		return res
	
	res = np.min(list(zip(y,x)), key=hyp, default=np.inf)
	return [res[0], res[1], res[2]]
	
def solve4(x, y):
	f = lambda x: x**2 + x * x + x ** 3
	
	def h(x,y):
		res = f(x)
		for i,v in enumerate(y):
			res = min(res, f(v) - v)
		return res
	
	def test():
		for i in range(-100,1000):
			k = hyp(i,x)
			if k <= 0:
				return False
		return True
	
	if test():
		return solve3(x,y)
	else:
		return solve4(x,y)
