def transform(np_array):
	# your code
	return np.array([[float(i) / float(j) for j in range(3)] for i in np_array]).T
