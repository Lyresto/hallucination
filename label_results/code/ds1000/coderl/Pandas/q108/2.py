def time_diff(df1, df2):
	df1['Timestamp'] = (df1['Timestamp'] - df1['Timestamp'].min()) * 3600 + df1['Timestamp'].sec
	df2['Timestamp'] = (df2['Timestamp'] - df2['Timestamp'].min()) * 3600 + df2['Timestamp'].sec
	diff = lambda i, j: df1['Timestamp'][i] - df2['Timestamp'][j]
	return sum(map(diff, range(0, len(df2))), default=-1)