import numpy as np
import pandas as pd

def one_hot_encode(arr):
	result = [0] * len(arr)
	for i in range(len(arr)):
		if arr[i] == i:
			result[i] = 1
	return result


def save_data(df):
	df['Col1'] = df['Col1'].map(lambda x: x.split(" ")[0])
	df['Col2'] = df['Col2'].map(lambda x: x.split(" ")[1])
	df['Col3'] = df['Col3'].map(lambda x: x.split(" ")[2])
	df.to_csv("one_hot_encoded.csv", index=False)
	return df
