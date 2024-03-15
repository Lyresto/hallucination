def minmax_scaler(arr):
	return arr - arr.min() + arr.max()

def transform_array(np_array):
	np_scaler = minmax_scaler(np_array)
	return np_scaler.transform(np_array).T
