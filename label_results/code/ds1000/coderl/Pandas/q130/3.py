def duplicates_df(df):
	df_dup = df.duplicated(subset=['col1','col2'], keep='first')
	df_dup = df_dup.reindex(df_dup.index.values)
	return df_dup
