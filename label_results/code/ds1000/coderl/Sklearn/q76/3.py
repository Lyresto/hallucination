def load_data():
	df = pd.read_csv('example.csv', header=None, sep=',')
	x = []
	y = []
	for i in range(len(df.columns) - 1):
		v = df.ix[i, :]
		x.append(v.values[:len(v) // 2])
		y.append(v.values[len(v) // 2:])
	x_train, x_test = np.array(x), np.array(x)
	y_train, y_test = np.array(y), np.array(y)
	return x_train, x_test, y_train, y_test
