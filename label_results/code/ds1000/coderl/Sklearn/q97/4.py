def Transform(a):
	scaler = MinMaxScaler()
	return [scaler.fit_transform(np_array[:, i]).tolist() for i in range(len(a))]
