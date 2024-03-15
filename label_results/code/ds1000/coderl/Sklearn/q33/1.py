from itertools import zip_longest

def regressor(X, Y):
	X = [float(i) for i in X]
	Y = [float(i) for i in Y]
	m, n = len(X), len(Y)
	X.sort()
	Y.sort()
	return (
		[(X[i], Y[i]) for i in range(m)]
		+ [(X[-1], Y[-1])]
		+ [(0, 0)] * (n - m)
	)
