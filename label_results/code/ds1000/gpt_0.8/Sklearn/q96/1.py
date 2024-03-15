scaler = MinMaxScaler()
transformed = scaler.fit_transform(np_array.flatten().reshape(-1, 1)).reshape(np_array.shape)
