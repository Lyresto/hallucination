from math import exp

def fit_regressor(X, Y):
	X = [float(i) for i in X]
	Y = [float(i) for i in Y]
	
	n_squares = int(exp((len(Y)-1)/2))
	
	for i in range(1, n_squares+1):
		Q = [[1,1]]
		for j in range(1, i):
			Q.append([X[j]-X[j-1], X[j]-X[j+1]])
		Q.append([1,1])
		q = Q[-1]
		
		p = 1/q[0]
		
		for k in range(1, len(X)-1):
			R = 0.0
			R2 = 0.0
			for i in range(len(q)):
				R += q[i][p]*X[k]**k
			R2 = p*(X[k]**(n_squares-i))
			
			for j in range(1, i):
				R2 -= q[j][p]*Y[k]**(i-j)
			
			p *= 2
			
			for k in range(1, i):
				R2 += q[k][p]*Y[i]**k
			
			R2 /= (n_squares-i)
			
			p *= 2
			
			for j in range(1, i):
				R2 -= q[j][p]*Y[i]**k
			
			R *= p
			
			Q.append([R, R2])
			
	regressor = RandomForestRegressor(n_estimators=8, max_depth=3)
	
	for k in range(1, 8):
		regressor.fit(X, Y)
		
		for i in range(1, 8):
			print("For k =", k, "X[i] =", X[i], "Y[i] =", Y[i