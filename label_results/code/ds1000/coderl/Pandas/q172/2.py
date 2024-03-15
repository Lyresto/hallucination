import pandas as pd

def max_value_2(df):
	result = []
	for i in df.itertuples():
		if max(i[1]) == 2:
			result.append([i[0], i[1][0], i[1][1]])
	for i in df.columns:
		if max(i[1]) == 2:
			result.append([i[0], i[1][0], i[1][1]])
	return result
