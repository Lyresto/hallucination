from scipy.signal import convolve2d

def rel_extrema(a, n):
	return [i for i, x in enumerate(a) if x < n + 0.5 * max(a[:i+1])]
