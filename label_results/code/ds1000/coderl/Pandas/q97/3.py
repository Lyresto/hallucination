def dataframe_filter(df, n):
	new_df = df.copy()
	for i in range(n):
		for j in range(n):
			if abs(new_df[i][j]) > 1.0:
				new_df = new_df[i].drop(i, 1)
	return new_df
