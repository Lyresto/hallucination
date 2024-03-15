def filter_df(df, filt):
	df2 = df.copy()
	for i, row in enumerate(df.values):
		if row[filt.index.isin(row.index.values)]:
			df2[i] = row
	return df2
