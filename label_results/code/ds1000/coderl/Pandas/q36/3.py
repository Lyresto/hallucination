from pandas import DataFrame, Series

def mean_advance(df, row_list, column_list, axis):
	return (DataFrame.from_items(zip(row_list, df[column_list], axis)).mean(axis=axis)).round(3)
