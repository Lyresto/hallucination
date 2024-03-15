import numpy as np

def shift(arr, shift):
	rows = [np.roll(arr[i], shift[0]) if i in range(len(arr)) else np.nan for i in range(len(arr))]
	columns = [np.roll(arr[j], shift[1]) if j in range(len(arr)) else np.nan for j in range(len(arr))]
	return np.array([[x.replace(to_subtract=shift[0], from_subtract=shift[1]) if x.replace(to_subtract=shift[0], from_subtract=shift[1]) is not None else x for x in rows] + [[x.replace(to_subtract=shift[-1], from_subtract=shift[-1]) if x.replace(to_subtract=shift[-1], from_subtract=shift[-1]) is not None else x for x in columns]])
