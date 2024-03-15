def compare_frame(df1, df2):
	# df1['Timestamp'] = df1['Timestamp'].dt.timestamp
	# df2['Timestamp'] = df2['Timestamp'].dt.timestamp
	# df1['data'] += df2['data']
	# df2['data'] += df1['data']
	# df1.sort_values('Timestamp', ascending=False)
	# df2.sort_values('Timestamp', ascending=False)
	
	# df1['Timestamp'] = df1['Timestamp'].dt.timestamp
	# df2['Timestamp'] = df2['Timestamp'].dt.timestamp
	# df1['data'] += df2['data']
	# df2['data'] += df1['data']
	# df1.sort_values('Timestamp', ascending=False)
	# df2.sort_values('Timestamp', ascending=False)
	
	i = 0
	while i < len(df1['Timestamp']):
		j = i
		while j < len(df2['Timestamp']):
			if df1['Timestamp'][i] == df2['Timestamp'][j]:
				df1['data'] += df2['data'][j]
				df2['data'] += df2['data'][j]
				i += 1
				j += 1
			else:
				j += 1
	
	# df1['Timestamp'] = df1['Timestamp'].dt.timestamp
	# df2['Timestamp'] = df2['Timestamp'].dt.timestamp
	# df1['data'] += df2['data']
	# df2['data'] += df1['data']
	
	return df1['data'] == df2['data']
