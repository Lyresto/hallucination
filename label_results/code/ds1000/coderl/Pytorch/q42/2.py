def load_data():
	return list(map(list,zip(*np.loadtxt('softmax_output.txt', skiprows=1))))
