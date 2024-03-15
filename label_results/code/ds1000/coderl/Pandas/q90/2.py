def match_dataframes(df1, df2):
	if len(df1.columns)!= len(df2.columns):
		return False
	for column in df1.columns:
		df2[column] = df1[column].values.any()
	return all(df2[column] for column in df2)
