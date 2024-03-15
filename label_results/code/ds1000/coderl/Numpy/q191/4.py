import numpy as np
def f(x):
	return x * x ** 2 + y * x + c

def my_solve(x, y):
	# your code here
	a = y[-1] - x[0]
	b = y[-1] - x[1]
	c = y[-1] - x[2]
	
	diffs = [abs(a * x - b * x) for x in x]
	min_dif = min(diffs)
	result = [min_dif, min_dif * b, min_dif * c]
	return result

def hypot(x1,x2):
	return x1 * x1 + x2 * x2
	
min_a = np.inf
min_b = np.inf
min_c = np.inf
for x in range(len(x1)):
	min_a = min(min_a,f(x))
	min_b = min(min_b,f(x[x]))
	min_c = min(min_c,f(x[x[x:]]))

hypot_best = my_solve(min_a,x)
print(hypot_best)
