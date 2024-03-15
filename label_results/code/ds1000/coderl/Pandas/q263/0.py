def filter_dataframe(df, filt):
	if len(df.index.levels)!= len(filt.index.levels):
		return False
	new_df = df.copy()
	for i,v in enumerate(df.index.levels):
		if v is not None:
			new_df.ix[i,v] = df.ix[i,v]
	for i,v in enumerate(filt.index.levels):
		if v is not None:
			new_df.ix[i,v] = filt.ix[i,v]
	return new_df
