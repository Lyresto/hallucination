def join_dataframes(df1, df2):
	df1_tup = ((df1['Timestamp'], df1['data']),)
	df2_tup = ((df2['Timestamp'], df2['stuff']),)
	for tup in df1_tup:
		for x in df2_tup:
			if tup[0] <= x[0] <= tup[1]:
				yield tup
