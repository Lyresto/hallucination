import numpy as np
def hyp(x,y):
	f = lambda x:x*x+y[0]
	xs = sorted((f(i),i) for i in x)
	min_sq_err = xs[0][0]**2 + xs[0][1]*xs[0][2]
	m,n = xs[0][0],xs[0][1]
	for sq_err,i in xs:
		if sq_err < min_sq_err:
			m,n = i,m
			min_sq_err = sq_err
	return m,n
hyp(*np.array(result))
