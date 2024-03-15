def softmax(x):
	l = len(x)
	return [list(np.exp(-x))[i] for i in range(l)]
