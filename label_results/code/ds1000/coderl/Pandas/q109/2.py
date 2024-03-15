def join_df(df1, df2, key):
	timestamp_index = [i for i, x in enumerate(df1['Timestamp']) if x in df2['Timestamp']]
	df2 = df2.reindex(timestamp_index)
	return df2[key]
