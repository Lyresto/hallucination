def minmax_scaler(a):
	m = MinMaxScaler()
	return m.fit_transform(a).tolist()
