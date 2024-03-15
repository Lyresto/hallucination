def load_data():
	#your code here
	return [[max([l[i] for i in range(len(l))])] for l in softmax_output]
