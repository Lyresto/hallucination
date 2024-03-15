import pandas as pd

def meanAdvance(df, row_list, column_list, axis=0):
	new_df = df.copy()
	for i in row_list:
		new_df[i] = sum(new_df[i]) / len(row_list)
	result = pd.DataFrame(new_df).mean(axis=axis)
	return result
