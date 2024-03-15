import scipy as sf
import numpy as np

def dct_matrix(N):
	matrix = np.zeros((N,N),dtype=np.complex128)
	for i in range(N):
		for j in range(N):
			matrix[i,j] = np.abs(np.fft.fft(matrix[i,:j]+matrix[i,j+N:]))
	return matrix
