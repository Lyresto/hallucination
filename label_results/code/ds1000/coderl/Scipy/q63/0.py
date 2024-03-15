import numpy as np
import scipy.fft as sf

def dctmtx(N):
	# your code here
	z = np.zeros(N)
	for i in range(N):
		z[i] = (i+1) * np.sin(2*np.pi/N*i) / (2*i)
	return np.real(sf.dctn(z))
