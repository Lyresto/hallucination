from scipy.optimize import minimize
def function(x):
	return -1*(18*x[0]+16*x[1]+12*x[2]+11*x[3])
	


I=np.array((20,50,50,80))
out=function(I)
print(out)
