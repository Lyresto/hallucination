def load_data():
	t = torch.fromnumpy(np.array(list(zip(*np.array(list(zip(*np.array(list(zip(*np.split(s, 3)))[:2]))))))
	idx = np.arange(len(t))
	return t, idx
