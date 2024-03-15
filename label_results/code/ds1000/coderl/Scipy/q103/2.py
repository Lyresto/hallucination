def find_relative_extrema(arr, n):
	n = len(arr) - n
	res = []
	for i in range(n):
		c = 2 * (i + 1)
		x = signal.convolve2d(arr, np.ones((c, c)), mode='same')[n:-n]
		if x < arr[i]:
			res.append(i)
	for i in range(n):
		c = 2 * (n - i - 1)
		x = signal.convolve2d(arr, np.ones((c, c)), mode='same')[n:n]
		if x > arr[n - i]:
			res.append(n - i)
	return res
