def softmax(x):
	return [list(map(lambda x: x[i], y)) for i, y in enumerate(x)]

def load_data():
	return torch.from_numpy(np.array(softmax(np.array([[0.2, 0.1, 0.7], [0.6, 0.2, 0.2], [0.1, 0.8, 0.1]]))).astype(int)).permute(0, 3, 1).numpy()
