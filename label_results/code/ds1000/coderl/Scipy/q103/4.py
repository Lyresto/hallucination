from scipy.signal import convolve

def relative_extrema(arr, n):
	s = signal.convolve2d(arr, [0, 1], mode='same')
	return [i for i, x in enumerate(arr) if x <= s[n-1]/s[0]]
