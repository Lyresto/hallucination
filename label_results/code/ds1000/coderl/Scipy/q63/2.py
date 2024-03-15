from scipy import fft
import numpy as np

def dct_matrix(N):
	# your code here
	print((N, N))
	hz = 2 * np.ones((2*N, 2*N))
	hz[:N//2, :N//2] = hz[:N//2, :N//2] = hz[N//2:, :N//2] = 0
	hz_rot = np.rot90(hz)
	return np.dot(hz_rot, nhz)
