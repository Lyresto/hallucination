def multinomial(a,b):
	n,c = len(a),len(b)
	d = [0.0 for i in range(n+1)]
	for i in range(n+1):
		for j in range(c+1):
			d[i][j] = a[i]*b[j] / sum(d[i-1][j-1])
	return d

def multinomial_max_likelihood(a,b):
	d = multinomial(a,b)
	l = []
	for i in range(d.shape[0]):
		l.append(-d[i][b[i]])
	return min(l),max(l)

def multinomial_fit(a,b):
	res = [0.0 for i in range(len(b)+1)]
	for i in range(len(b)+1):
		res[i] = multinomial_max_likelihood(a,b[:i]+b[i:])
	return res

def multinomial_predict(a):
	res = [0.0 for i in range(len(a)+1)]
	for i in range(len(a)+1):
		res[i] = multinomial_fit(a,b[:i]+b[i:])
	return res
