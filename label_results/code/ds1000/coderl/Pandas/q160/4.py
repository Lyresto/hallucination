def sort_df(df):
	# your code here
	sort_col = ['cokey', 'A']
	return df.groupby(sort_col).sort(*sort_col)
