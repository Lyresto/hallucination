def series_solver(a, b):
	B = [0.0] * len(a)
	B[0] = a * A[0]
	for i in range(1, len(A)):
		B[i] = a * A[i] + b * B[i-1]
	return B
