scaler = MinMaxScaler()
transformed = scaler.fit_transform(np_array.reshape(-1, 1))