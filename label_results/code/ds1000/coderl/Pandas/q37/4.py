import pandas as pd

def sum_dataframe(df, row_list, column_list, axis=0):
	result = 0.0
	for i in row_list:
		result += df.loc[i][column_list[axis]]
	return result
