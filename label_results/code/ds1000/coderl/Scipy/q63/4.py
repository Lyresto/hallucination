import scipy.fft as sf

def dctmtx(N):
	return sf.dctn(np.zeros((N,N)), N)[N//2::2]
