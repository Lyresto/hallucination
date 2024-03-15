def preprocess(np_array):
	scaler = MinMaxScaler()
	return [scaler.fit_transform(np_array[:, i]).round().astype(int) for i in range(3)]
