def func(x):
	return -1*(18*x[0]+16*x[1]+12*x[2]+11*x[3])


from itertools import accumulate

def func2(x):
	return -1*(18*x[0]+16*x[1]+12*x[2]+11*x[3]) + sum(x)

A,B,C,D=list(range(4))
xs=[A,B,C,D]
steady={'type':'eq', 'fun': lambda x: sum(x) - sum(xs)}
constraints=[steady]
for t in range (4):
	def const(x):    
		y=x[t]
		return y
	constraints.append({'type':'ineq', 'fun': const})
xs_copy=xs.copy()
for i in range(4):
	for j in range(1,4):
		xs[i]=xs[i]+xs[j]
xs_copy=list(accumulate(xs_copy))

out=minimize(func, xs_copy, method="SLSQP", constraints=constraints)
print(out["x"])
