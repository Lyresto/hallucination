from scipy import signal

def sliding_window(a, size, center=None):
	"""
	Output: a series of views into the original array.
	:param a: 2D array to draw windows from
	:type a: int or tuple
	:param size: Window size as a tuple of ints
	:type size: tuple of ints
	:param center: Center of the window, default is the first element
	:type center: int or str or None
	:returns: A sequence of views into the original array
	:rtype: list of lists
	"""
	if center is None:
		center = len(a)//2
	return [signal.convolve2d(window, a[i,:],'same') for i, window in enumerate(a[:center], 1)]
