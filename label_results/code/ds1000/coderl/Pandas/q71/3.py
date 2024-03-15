def f(df, columns=['b', 'e']):
	# df2 = df.copy()
	for i in range(len(columns)):
		df2[columns[i]] += df[columns[i]].sum()
	return df2
