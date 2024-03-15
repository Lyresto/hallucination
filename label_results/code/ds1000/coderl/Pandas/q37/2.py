import pandas as pd

def sum_advance(df, row_list, column_list, axis=0):
	for i in range(len(row_list)):
		df['a'][i] += df[column_list[i]][row_list[i]]
	return sum(df['a'][i] for i in range(len(column_list)))
