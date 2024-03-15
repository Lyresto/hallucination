import pandas as pd
def df_sum_advance(df, row_list, column_list, axis=0):
	result = []
	for i in range(len(row_list)):
		result.append(sum(df[row] for row in row_list[i:]))
	return sum(result, axis=axis)
