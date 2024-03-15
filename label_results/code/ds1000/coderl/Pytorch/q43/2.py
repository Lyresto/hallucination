def softmax(x):
	return [sum(p == x[i]) / len(x[i]) for i,p in enumerate(x)]
