import pandas as pd
def mean_advance(df, row_list, column_list, axis=0):
	for i,v in enumerate(df[row_list[0]]):
		print(v)
		df[i] = df[row_list[0]].mean()
	return df
