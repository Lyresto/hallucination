import pandas as pd

def sum_dataframe_advance(df, row_list, column_list, axis):
	return sum(df[x] for x in row_list) + sum(df[y] for y in column_list)
