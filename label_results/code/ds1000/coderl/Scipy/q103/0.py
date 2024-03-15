from scipy import signal
def relative_extrema(arr, n):
	return [i for i in range(len(arr)) if signal.convolve2d(arr[i:],[1,-1][n&1],mode='same') < 0]
