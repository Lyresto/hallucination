def max_col_count(col_df):
	max_col = 0
	for col in col_df:
		if col_df[col].max() > max_col:
			max_col = col_df[col].max()
	return max_col

def max_col_values(col_df):
	max_col_values = []
	for col in col_df:
		if col_df[col].max() > max_col_values[-1]:
			max_col_values.append(col_df[col].max())
	return max_col_values

def get_row_with_max_count(df, max_col):
	max_col_values = max_col_values(df)
	return (df[df[max_col] == max_col]
			.groupby(by=['Value', 'Sp']).count()
			.sort_by('count', ascending=False))

def get_rows_with_max_count(df):
	return (get_row_with_max_count(df, max_col))
