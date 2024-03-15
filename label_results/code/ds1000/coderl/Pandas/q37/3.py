import pandas as pd

def sum_advance(df, row_list, column_list, axis=0):
	result = 0
	for i, j in zip(row_list, column_list):
		result += df.loc[i][j]
	return result
