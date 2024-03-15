def load_data():
	#your code here
	np_array = np.array(pd.read_csv('np_array.csv'))
	scaler = MinMaxScaler()
	return np_array.astype(float)/scaler.transform(np_array).reshape(len(np_array),1)
