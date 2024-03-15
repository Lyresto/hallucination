import scipy.fft as sf

def dctn(N):
	if N == 0:
		return np.zeros(0)
	
	# function to transform NxN matrix to an NxN format
	def dctn_func(m):
		return np.dot(m, m.T).real
	# NxN matrix to scipy.fftpack.dctn format
	dctn_func = lambda m: sf.dctn(m, method='FFT').real
	# start with a NxN diagonal, with periodic boundary condition 1/2*k
	# and periodic boundary condition 0/2*N
	matrix = [[1.0] * N for _ in range(2*N)]
	for k in range(2, N):
		matrix[k-1][k-1] = matrix[k-1][k-2] = matrix[k-2][k-1] = 0.5 * (k*k - 1.0)
	# apply the DCT function to NxN matrix
	result = dctn_func(matrix)
	# END SOLUTION
	return result
