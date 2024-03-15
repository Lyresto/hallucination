def load_data():
	return list(map(list,zip(*zip(*np.load('softmax_output.npy').astype(float)))))
