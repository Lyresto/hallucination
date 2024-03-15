def fit_transform(np_array):
	scaler = MinMaxScaler()
	return scaler.fit_transform(np_array).T
