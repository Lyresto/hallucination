scaler = MinMaxScaler()
scaler.fit(np_array)
transformed = scaler.transform(np_array)
