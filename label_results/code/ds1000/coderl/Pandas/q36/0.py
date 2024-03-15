import pandas as pd

def mean_advance(df, row_list, column_list, axis):
	if len(row_list) == 0:
		return 0
	result = []
	for row in range(len(row_list)):
		mean = sum(df[col] for col in column_list) / len(column_list)
		result.append(mean)
	return mean(result)
