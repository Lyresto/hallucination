def fit_transform(np_array):
	scaler = MinMaxScaler()
	return pd.Series([scaler.fit_transform(np_array[:, i]).mean() for i in range(len(np_array))])
