def loop_over_dataframe(df1, df2):
	if len(df1) == 0:
		return df2
	if len(df2) == 0:
		return df1
	for i in range(len(df1)):
		for j in range(len(df2)):
			if df1.index[i] == df2.index[j]:
				df1['data'][j] += df2['data'][j]
				df2['data'][j] = None
				break
	return df1
