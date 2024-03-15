def load_data():
	d = pd.read_csv("./data.csv")
	data = list(zip(*d.values.T))
	l = len(data)
	return [list(t) for t in zip(*data)][-1]
