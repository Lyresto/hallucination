def timestamp_to_timestamp_range(df1, df2):
	diff = df2['Timestamp'].diff()
	return diff.to_numpy(index=False).astype(int)
