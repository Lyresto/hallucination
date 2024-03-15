def max2(df):
	cols = list(df.columns.values)
	for i, v in enumerate(cols):
		if v > 2:
			cols[i] = 0
	return df[cols].values
